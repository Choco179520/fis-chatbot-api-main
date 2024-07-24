module.exports = {
    apps: [
      {
        name: 'fis-chatbot-api-main',
        script: './app.py',
        interpreter: 'python3', // Usa 'python' si tu Python está en esa versión
        watch: true, // Opcional: reinicia si hay cambios en el script
        autorestart: true,
        instances: 1, // Número de instancias (o 'max' para el máximo número de instancias posibles)
      },
    ],
  };
  