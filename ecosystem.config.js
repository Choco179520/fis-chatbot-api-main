module.exports = {
    apps: [
      {
        name: 'fis-chatbot-api-main',
        script: './app.py',
        interpreter: 'python3', // Usa 'python' si tu Python está en esa versión
        watch: true, // Opcional: reinicia si hay cambios en el script
        autorestart: true,
        instances: 1, // Número de instancias (o 'max' para el máximo número de instancias posibles)
        env: {
            HOST:'localhost',
            PORT:'3001',
            MAX_USER_MESSAGE_LENGTH:'200',
            MAX_SUGGESTIONS_NUMBER:'2',
            SYNTAX_CLEANER:'True',
            STOP_WORDS_CLEANER:'False',
            LEMMATIZER:'False',
            CONFIDENCE_LIMIT:'0.70',
            SUGGESTION_LIMIT:'0.60',            
            BASE_MODEL:'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2',
            FINED_TUNED_MODEL:'fis-chatbot/tuned-api-core',
            MODEL_TOKEN:'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',
            UTTERANCES_LIMIT:'5',
            BATCH_SIZE:'16',
            EPOCHS:'12',
            DB_URL: 'http://localhost:3000/api'
          }
      },
    ],
  };
  