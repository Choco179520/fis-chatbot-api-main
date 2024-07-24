import csv
import os

from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set working directories
current_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(current_path)
fined_tuned_model_path = f"{root_path}/models/{os.getenv('FINED_TUNED_MODEL')}"
training_examples_path = f"{root_path}/training/examples/fis-examples.csv"

def fit_base_model():
    # Load base pretrained model
    base_model = SentenceTransformer(os.getenv('BASE_MODEL'))

    # Get documents from a database
    from static.documents import documents
    documents: list[dict] = documents.documents

    # Load training examples
    try:
        _validate_training_examples(documents)
        train_data = _get_examples_train_data()

        # noinspection PyTypeChecker
        train_dataloader = DataLoader(train_data, shuffle=True, batch_size=int(os.getenv('BATCH_SIZE')))
        cosine_loss = losses.CosineSimilarityLoss(model=base_model)

        # Fit model with the training examples
        base_model.fit(
            train_objectives=[(train_dataloader, cosine_loss)],
            epochs=int(os.getenv('EPOCHS')),
            optimizer_params={'lr': 2e-5},
            show_progress_bar=True,
            warmup_steps=100,
        )

        return base_model
    except Exception as exception:
        print(exception)
        return


def _get_examples_train_data():
    train_data = []

    with open(training_examples_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            if len(row) >= 3:
                base_text = row[0].strip()
                alternative_text = row[1].strip()
                similarity = row[2].strip()

                try:
                    similarity_float = float(similarity)
                except ValueError:
                    raise Exception('An error occurred while obtaining the training examples.')

                input_example = InputExample(texts=[base_text, alternative_text], label=similarity_float)
                train_data.append(input_example)

    return train_data


def _validate_training_examples(documents: list[dict]):
    with open(training_examples_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            similarity = row[2].strip()

            try:
                float(similarity)
            except ValueError:
                raise Exception('An error occurred while validating the training examples.')


if __name__ == '__main__':
    fined_tuned_model = fit_base_model()

    if fined_tuned_model:
        fined_tuned_model.save(fined_tuned_model_path, 'fis-tuned-model')
    else:
        print('An error occurred while training the model.')
