special_enrollment = {
    "id": "matricula-especial",
    "title": "Matrícula Especial",
    "utterances": [
        "Matrícula Especial",
        "¿Qué es una matrícula especial?",
        "¿Para que sirve una matrícula especial?",
        "¿Cuando se puede pedir una matrícula especial?",
        "¿Quién puede solicitar una matrícula especial?",
        "Necesito una matrícula especial",
        "Me gustaría solicitar una matrícula especial",
        "¿Cuando es posible solicitar una matrícula especial?",
        "¿En qué casos puedo pedir una matrícula especial?",
        "Creo que necesito pedir una matrícula especial",
    ],
    "responses": [
        {
            "type": "text",
            "content": "Si no te inscribiste durante \"Matrículas Ordinarias o Extraordinarios\" debido a "
                       "circunstancias administrativas o por casos de fuerza mayor puedes "
                       "solicitar una \"Matrícula Especial\"."
        },
        {
            "type": "text",
            "content": "Recuerda revisar los plazos para solicitar una \"Matrícula Especial\" "
                       "el Calendario Académico disponible en el siguiente enlace:"
        },
        {
            "type": "link",
            "path": "https://www.epn.edu.ec/admision/calendario-academico-propedeutico-nivelacion/",
            "name": "Calendarios Académicos"
        },
        {
            "type": "text",
            "content": "Si quieres conocer el procedimiento para solicitar una \"Matrícula Especial\" puedes "
                       "hacerlo mediante el siguiente mensaje:"
        },
        {
            "type": "action",
            "action": "proceso-matricula-especial",
            "name": "Proceso para una Matrícula Especial"
        },
    ]
}

special_enrollment_process = {
    "id": "proceso-matricula-especial",
    "title": "Proceso para una Matrícula Especial",
    "utterances": [
        "Proceso para una Matrícula Especial",
        "¿Qué debo hacer para pedir una matrícula especial?",
        "Pasos para solicitar una matrícula especial",
        "¿Cómo solicito una matrícula especial?",
        "Formulario para solicitar una matrícula especial",
        "¿Cómo me inscribo durante matrículas especiales?",
        "Pedir una matrícula especial por casos de fuerza mayor",
        "Pedir una matrícula especial por situaciones administrativas",
        "¿Cómo pido una matrícula especial por casos de fuerza mayor?",
        "¿Cómo pido una matrícula especial por casos de situaciones administrativas?",
    ],
    "responses": [
        {
            "type": "text",
            "content": "Para solicitar una \"Matrícula Especial\" por casos de fuerza mayor debes completar "
                       "y obligatoriamente documentar el formulario F_AA_113 disponible en el siguiente enlace:"
        },
        {
            "type": "link",
            "path": "https://atenea.epn.edu.ec/handle/25000/222",
            "name": "Formulario F_AA_113"
        },
        {
            "type": "text",
            "content": "Para solicitar una \"Matrícula Especial\" por situaciones administrativas de la "
                       "institución simplemente debes entregar el formulario F_AA_113 en el Decanato."
        },
        {
            "type": "text",
            "content": "Recuerda revisar los plazos para solicitar una \"Matrícula Especial\" "
                       "el Calendario Académico:"
        },
        {
            "type": "link",
            "path": "https://www.epn.edu.ec/admision/calendario-academico-propedeutico-nivelacion/",
            "name": "Calendarios Académicos"
        }
    ]
}
