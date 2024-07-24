regular_enrollment = {
    "id": "matricula-ordinaria",
    "title": "Matrícula Ordinaria",
    "utterances": [
        "Matrícula Ordinaria",
        "¿Qué es una matrícula ordinaria?",
        "¿Cuando se realizan las matrículas ordinarias?",
        "¿En qué fechas inician las matrículas ordinarias?",
        "Fechas de las actividades para matrículas ordinarias",
        "No sé lo que es una matrícula ordinaria",
        "Cuando inicia el periodo de matrículas ordinarias",
        "¿Estoy dentro del plazo para pedir una matrícula ordinaria?",
        "¿Estoy a tiempo de una matrícula ordinaria?",
        "Calendario académico para matrículas ordinarias"
    ],
    "responses": [
        {
            "type": "text",
            "content": "La \"Matrícula Ordinaria\" se realiza antes del inicio de clases "
                       "según las fechas establecidas en el Calendario Académico y en la "
                       "planificación de actividades:"
        },
        {
            "type": "image",
            "path": "ordinary_registration_activities.png",
            "alt": "Actividades relacionadas a la \"Matrícula Ordinaria\""
        },
        {
            "type": "text",
            "content": "Puedes revisar el Calendario Académico en el siguiente enlace:"
        },
        {
            "type": "link",
            "path": "https://www.epn.edu.ec/admision/calendario-academico-propedeutico-nivelacion/",
            "name": "Calendarios Académicos"
        },
        {
            "type": "text",
            "content": "Recuerda revisar los requisitos y actividades para acceder a una \"Matrícula Ordinaria\":"
        },
        {
            "type": "action",
            "action": "requisitos-matricula-ordinaria",
            "name": "Requisitos de una Matrícula Ordinaria"
        },
        {
            "type": "action",
            "action": "proceso-matricula-ordinaria",
            "name": "Procedimiento para una Matrícula Ordinaria"
        }
    ]
}

regular_enrollment_requirements = {
    "id": "requisitos-matricula-ordinaria",
    "title": "Requisitos de una Matrícula Ordinaria",
    "utterances": [
        "Requisitos de una Matrícula Ordinaria",
        "¿Cómo se accede a una matrícula ordinaria",
        "¿Qué requisitos necesito para matricularme?",
        "¿Debo hacer algo para poder matricularme?",
        "¿Que debo cumplir para la matrícula ordinaria?",
        "¿Debo hacer algo antes de matricularme?",
        "Quiero saber los requisitos para matricularme",
        "Pasos previos para una matrícula ordinaria",
        "Requisitos para una matrícula ordinaria",
        "¿Necesito algo para poder matricularme?"
    ],
    "responses": [
        {
            "type": "text",
            "content": "Antes del proceso de \"Matrículas Ordinarias\" obligatoriamente debes realizar "
                       "las siguientes actividades:"
        },
        {
            "type": "text",
            "content": "1. Completar la encuesta de preplanificación que se envía al correo institucional."  # noqa
        },
        {
            "type": "text",
            "content": "2. Comprobar que no te encuentres inhabilitado para realizar trámites públicos."
        },
        {
            "type": "text",
            "content": "3. Realizar un control de documentos en la Secretaría del Subdecanato. "
                       "Se te enviará un correo cuando este procedimiento se realice."
        },
        {
            "type": "text",
            "content": "4. Revisar las fechas asignadas a las actividades de la "
                       "\"Matrícula Ordinaria\" en el Calendario Académico:"
        },
        {
            "type": "link",
            "path": "https://www.epn.edu.ec/admision/calendario-academico-propedeutico-nivelacion/",
            "name": "Calendarios Académicos"
        },
        {
            "type": "text",
            "content": "Consultar en el sistema SAEw el turno (fecha y hora) asignado para tu matrícula."
        },
    ]
}

regular_enrollment_process = {
    "id": "proceso-matricula-ordinaria",
    "title": "Procedimiento para una Matrícula Ordinaria",
    "utterances": [
        "Procedimiento para una Matrícula Ordinaria",
        "¿Cuál es el procedimiento de matrícula?",
        "¿Cómo puedo matricularme?",
        "¿Qué pasos debo seguir para matricularme?",
        "Proceso para una matrícula ordinaria",
        "No sé que hacer para matricularme",
        "Quiero saber los pasos para matricularme",
        "¿Qué se hace durante una matrícula ordinaria?",
        "¿Qué pasa si no logré inscribirme en todas las materias?",
        "No hay cupo en las materias"
    ],
    "responses": [
        {
            "type": "text",
            "content": "Durante las fechas de \"Matrículas Ordinarias\" debes inscribirte directamente en "
                       "el sistema SAEw en la fecha y horas que se te asignaron."
        },
        {
            "type": "text",
            "content": "Si no lograste inscribirte en todas las asignaturas, debes inscribirte en al "
                       "menos una de ellas para que posteriormente accedas a una \"Matrícula Ordinaria Asistida\"."
        },
        {
            "type": "text",
            "content": "Recuerda revisar los requisitos para acceder a una \"Matrícula Ordinaria\":"
        },
        {
            "type": "action",
            "action": "acceso-matricula-ordinaria",
            "name": "Requisitos de una Matrícula Ordinaria"
        },
    ]
}

assisted_regular_enrollment = {
    "id": "matricula-ordinaria-asistida",
    "title": "Matrícula Ordinaria Asistida",
    "utterances": [
        "Matrícula Ordinaria Asistida",
        "¿Qué es una matrícula asistida?",
        "¿Cuando debo pedir una matrícula asistida?",
        "Quiero una matrícula asistida",
        "Necesito una matrícula asistida",
        "No pude inscribirme en todas las asignaturas",
        "No hubo cupo en todas mis asignaturas",
        "¿Cómo solicito una matrícula asistida?",
        "¿Cómo se realiza una matrícula asistida?",
        "Me gustaría una matrícula asistida"
    ],
    "responses": [
        {
            "type": "text",
            "content": "Si no lograste inscribirte en todas las asignaturas, pero al menos te inscribiste "
                       "en una de ellas puedes acceder a una \"Matrícula Asistida\"."
        },
        {
            "type": "text",
            "content": "Para ello, debes acudir presencialmente a la Secretaría del Subdecanato "
                       "durante las fechas asignadas en el Calendario Académico:"
        },
        {
            "type": "link",
            "path": "https://www.epn.edu.ec/admision/calendario-academico-propedeutico-nivelacion/",
            "name": "Calendarios Académicos"
        },
    ]
}
