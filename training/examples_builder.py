import csv
import os

# Set working directories
current_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(current_path)
training_examples_path = f"{root_path}/training/examples/fis-examples-primary.csv"

def _create_csv(list_of_lists, file_name):
    headers = ['primary_sentence', 'secondary_sentence', 'label']

    with open(file_name, 'w', newline='', encoding="utf-8") as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write headers in the first row
        csv_writer.writerow(headers)
        
        # Write each inner list to the CSV file
        for inner_list in list_of_lists:
            primary_sentence, secondary_sentence = inner_list
            csv_writer.writerow([primary_sentence, secondary_sentence, ''])


def _get_unique_pairs(document_utterances, document_relevant_utterances) -> list[list[str]]:
    unique_sentences_pairs = []

    for sentence in document_relevant_utterances:
        for pair_sentence in document_utterances:
            if sentence != pair_sentence:
                unique_pair = [sentence, pair_sentence]
                if unique_pair not in unique_sentences_pairs and unique_pair[::-1] not in unique_sentences_pairs:
                    unique_sentences_pairs.append(unique_pair)

    return unique_sentences_pairs


if __name__ == '__main__':
    processed_documents: list[str] = []
    primary_pairs: list[list[str]] = []

    # Get documents from a database
    from static.documents import documents
    documents: list[dict] = documents.documents

    # Get most relevant utterances per document
    from examples.relevant_utterances import relevant_utterances

    for document in documents:
        # Search most relevance document of the current document
        found_document = None
        for current_document in relevant_utterances:
            if current_document.get('document_id') == document['id']:
                found_document = current_document
                break

        # Get sentences unique pairs
        sentence_pairs = _get_unique_pairs(document['utterances'], found_document['relevant_utterances'])
        primary_pairs = primary_pairs + sentence_pairs

    # Get pairs of most relevant utterances
    secondary_pairs: list[list[str]] = []

    for i, current_document in enumerate(relevant_utterances):
        for utterance in current_document['relevant_utterances']:
            for j, next_document in enumerate(relevant_utterances):
                if i != j:
                    for pair_utterance in next_document['relevant_utterances']:
                        pair = [utterance, pair_utterance]
                        if pair not in secondary_pairs and pair[::-1] not in secondary_pairs:
                            secondary_pairs.append(pair)

    pairs = primary_pairs + secondary_pairs

    _create_csv(pairs, training_examples_path)
