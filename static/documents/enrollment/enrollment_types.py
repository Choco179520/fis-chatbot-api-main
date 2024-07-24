enrollment_types = {
    "id": "tipos-matriculas",
    "title": "Tipos de Matrículas",
    "utterances": [
        "Tipos de Matrículas",
        "¿Qué tipos de matrículas existen?",
        "¿A qué matrículas puedo acceder?",
        "¿Que matrículas puedo solicitar?",
        "Quiero saber que matrículas existen",
        "Necesito una matrícula específica",
        "Me gustaría pedir una matrícula específica",
        "¿Aún existe la matrícula excepcional?",
        "Quiero una matrícula excepcional",
        "¿Puedo solicitar una matrícula excepcional?"
    ],
    "responses": [
        {
            "type": "text",
            "content": "Durante este periodo académico existen tres tipos de matrículas disponibles: "
                       "\"Matrícula Ordinaria\", \"Matrícula Extraordinaria\" y \"Matrícula Especial\"."
        },
        {
            "type": "text",
            "content": "Si necesitas conocer más detalles sobre algún tipo de matrícula puedes "
                       "hacerlo mediante los siguientes mensajes:"
        },
        {
            "type": "action",
            "action": "matricula-ordinaria",
            "name": "Matrícula Ordinaria"
        },
        {
            "type": "action",
            "action": "matricula-extraordinaria",
            "name": "Matrícula Extraordinaria"
        },
        {
            "type": "action",
            "action": "matricula-especial",
            "name": "Matrícula Especial"
        },
    ]
}
