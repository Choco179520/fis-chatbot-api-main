undergraduate_reentry_process = {
    "id": "proceso-reingreso-pregrado",
    "title": "Proceso de Reingreso a Pregrado",
    "utterances": [
        "Proceso de Reingreso a Pregrado",
        "Abandoné la carrera y quiero regresar",
        "Quiero volver a entrar a mi carrera",
        "Necesito regresar a mi carrera",
        "Me gustaría volver a la universidad",
        "Quiero retomar mis estudios",
        "¿Cómo puedo volver a mi carrera?",
        "Necesito información sobre el reingreso",
        "¿Qué debo hacer para regresar a mi carrera?",
        "Necesito ayuda para volver a mi carrera"
    ],
    "responses": [
        {
            "type": "text",
            "content": "Para solicitar el reingreso a una carrera de tercer nivel debes completar "
                       "el formulario F_AA_201 disponible en el siguiente enlace:"
        },
        {
            "type": "link",
            "path": "https://atenea.epn.edu.ec/handle/25000/227",
            "name": "Enlace al Formulario F_AA_201"
        },
        {
            "type": "text",
            "content": "Luego, debes entregar el formulario en la secretaría del Subdecanato."
        },
        {
            "type": "text",
            "content": "Recuerda revisar los procesos de validación "
                       "de datos socioeconómicos para el proceso de reingreso:"
        },
        {
            "type": "action",
            "action": "datos-socioeconomicos-reingreso-pregrado",   # noqa
            "name": "Datos Socioeconómicos para el Reingreso a Pregrado"
        }
    ]
}

socioeconomic_data_to_undergraduate_reentry_process = {    # noqa
    "id": "datos-socioeconomicos-reingreso-pregrado",   # noqa
    "title": "Datos Socioeconómicos para el Reingreso a Pregrado",
    "utterances": [
        "Datos Socioeconómicos para el Reingreso a Pregrado",
        "¿Necesito actualizar mis datos socioeconómicos para volver a mi carrera?",
        "Quiero saber si necesito algo para volver a la universidad",
        "¿Qué requisitos necesito para regresar a mi carrera?",
        "¿Debo actualizar mis datos socioeconómicos para regresar a mi carrera?",
        "¿Qué debo tener en cuenta para volver a mi carrera?",
        "Cosas a tener en cuenta para regresar a una carrera",
        "¿Para regresar a mi carrera necesito actualizar mis datos socioeconómicos?",
        "¿Cómo se si puedo volver a mi carrera?",
        "Quiero saber si podré volver a mi carrera"
    ],
    "responses": [
        {
            "type": "text",
            "content": "Para solicitar el reingreso a una carrera de tercer nivel debes tomar en cuenta que:"
        },
        {
            "type": "text",
            "content": "1. Si previamente ingresaste tus datos socioeconómicos, esa información servirá "
                       "para tu reingreso. Sin embargo, si quieres actualizar tu información puedes utilizar "
                       "el formulario F_AA_117 disponible en el siguiente enlace:"
        },
        {
            "type": "link",
            "path": "https://atenea.epn.edu.ec/handle/25000/502",
            "name": "Enlace al Formulario F_AA_117"
        },
        {
            "type": "text",
            "content": "2. Si aún no has registrado tus datos socioeconómicos tu ingreso será habilitado. "
                       "Luego de lo cual, debes registrar la información necesaria mediante el formulario F_AA_117."
        },
        {
            "type": "text",
            "content": "Ten en cuenta que al actualizar o ingresar tu información por primera vez es "
                       "necesario que el personal de la institución lo valide. Puedes encontrar información "
                       "para contactarte con el personal de validación en el siguiente enlace:"
        },
        {
            "type": "link",
            "path": "https://atenea.epn.edu.ec/handle/25000/519",
            "name": "Guía para Validación de Datos Socioeconómicos"
        },
    ]
}
