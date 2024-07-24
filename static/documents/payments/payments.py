payment_selection = {
    "id": "seleccionar-partes-pago",
    "title": "Cómo Seleccionar el Número de Partes para el Pago",
    "utterances": [
        "Cómo Seleccionar el Número de Partes para el Pago",
        "¿Cómo puedo seleccionar el número de partes para el pago de matrícula?",
        "Quiero saber cómo dividir el pago de la matrícula",
        "Instrucciones para elegir las cuotas de pago de matrícula",
        "¿Cómo elijo las cuotas para la matrícula?",
        "¿Cómo fracciono el pago de la matrícula?",
        "Explícame cómo dividir el costo de la matrícula",
        "¿Cuáles son las instrucciones para el pago fraccionado de la matrícula?",
        "¿Puedo saber cómo seleccionar el número de partes para la matrícula?",
        "Instrucciones para dividir el pago de la matrícula, ¿por favor?",
    ],
    "responses": [
        {
            "type": "text",
            "content": "Para seleccionar el número de partes para el pago de tu matrícula, "
                       "consulta el manual de usuario en el siguiente enlace."
        },
        {
            "type": "link",
            "path": "https://atenea.epn.edu.ec/handle/25000/516",
            "name": "Manual de Usuario - Pago de Matrícula"
        },
        {
            "type": "action",
            "action": "fechas-pago-retrasos",
            "name": "Fechas de Pago y Consecuencias de Retrasos"
        },
        {
            "type": "action",
            "action": "facturacion-pagos-saew",
            "name": "Facturación y Pagos en el Sistema SAEw"
        }
    ]
}

payment_dates_delays = {
    "id": "fechas-pago-retrasos",
    "title": "Fechas de Pago y Consecuencias de Retrasos",
    "utterances": [
        "Fechas de Pago y Consecuencias de Retrasos",
        "¿Cuáles son las fechas para pagar las cuotas de matrícula?",
        "¿Qué pasa si me retraso en el pago de una cuota?",
        "Información sobre fechas de pago y penalizaciones por retraso",
        "¿Cuándo vencen las fechas de pago de las cuotas de matrícula?",
        "En caso de retraso en el pago de una cuota, ¿qué consecuencias hay?",
        "Necesito detalles sobre las fechas de pago y las penalizaciones por retraso",
        "¿Cuáles son las fechas límite para abonar las cuotas de matrícula?",
        "¿Qué sucede si no cumplo con la fecha de pago de una cuota?",
        "Información acerca de las fechas de pago y las sanciones por demora",
    ],
    "responses": [
        {
            "type": "text",
            "content": "Las fechas para realizar los pagos de tu matrícula, si has solicitado el pago en partes, "
                       "son las siguientes. Recuerda que el pago puntual es necesario para evitar recargos."
        },
        {
            "type": "image",
            "path": "payment_dates_delays.png",
            "alt": "Calendario de Fechas de Pago de Cuotas"
        },
        {
            "type": "action",
            "action": "politica-recargos-retraso",
            "name": "Política de Recargos por Retraso en el Pago de Cuotas"
        },
        {
            "type": "action",
            "action": "seleccionar-partes-pago",
            "name": "Cómo Seleccionar el Número de Partes para el Pago"
        }
    ]
}

policy_surcharges_delay = {
    "id": "politica-recargos-retraso",
    "title": "Política de Recargos por Retraso en el Pago de Cuotas",
    "utterances": [
        "Política de Recargos por Retraso en el Pago de Cuotas",
        "¿Cuánto es el recargo por retraso en el pago de cuotas?",
        "¿Qué sucede si no pago una cuota a tiempo?",
        "Información sobre recargos por retraso en pagos",
        "Explíqueme la política de recargos por retraso en el pago de cuotas",
        "¿Cuál es el monto del recargo por demora en el pago de cuotas?",
        "¿Cuáles son las consecuencias si no pago una cuota puntualmente?",
        "Necesito detalles sobre los recargos por retraso en los pagos",
        "¿Qué políticas aplican en caso de retraso en el pago de cuotas?",
        "Información acerca de los recargos por demora en los pagos",
    ],
    "responses": [
        {
            "type": "text",
            "content": "Si no realizas el pago de la segunda, tercera o cuarta cuota en "
                       "las fechas establecidas, incurrirás en un recargo del 10% de la cuota. "
                       "Este recargo se añadirá al monto de la siguiente cuota."
        },
        {
            "type": "action",
            "action": "dificultades-economicas-cuotas",
            "name": "Qué Hacer en Caso de Dificultades Económicas para Pagar Cuotas"
        },
        {
            "type": "action",
            "action": "fechas-pago-retrasos",
            "name": "Fechas de Pago y Consecuencias de Retrasos"
        }
    ]
}

economic_difficulties_quotas = {
    "id": "dificultades-economicas-cuotas",
    "title": "Qué Hacer en Caso de Dificultades Económicas para Pagar Cuotas",
    "utterances": [
        "Qué Hacer en Caso de Dificultades Económicas para Pagar Cuotas",
        "¿Qué puedo hacer si no tengo el dinero para pagar una cuota?",
        "¿Hay alguna opción si no puedo pagar la cuota a tiempo por problemas económicos?",
        "Soluciones para dificultades económicas en el pago de cuotas",
        "¿Alternativas si no tengo dinero para una cuota?",
        "¿Soluciones para problemas económicos en el pago?",
        "¿Cómo actuar si no pago la cuota a tiempo?",
        "Instrucciones para dificultades económicas en cuotas",
        "¿Hay opciones si no puedo pagar la cuota por problemas financieros?",
        "¿Qué hacer en caso de dificultades económicas con el pago de cuotas?",
    ],
    "responses": [
        {
            "type": "text",
            "content": "Si enfrentas dificultades económicas y no puedes pagar la segunda, "
                       "tercera o cuarta cuota en las fechas establecidas, puedes hacerlo en las fechas del "
                       "Calendario Académico para la siguiente cuota, con el recargo respectivo."
        },
        {
            "type": "action",
            "action": "facturacion-pagos-saew",
            "name": "Facturación y Pagos en el Sistema SAEw"
        },
        {
            "type": "action",
            "action": "politica-recargos-retraso",
            "name": "Política de Recargos por Retraso en el Pago de Cuotas"
        }
    ]
}

billing_payments_saew = {
    "id": "facturacion-pagos-saew",
    "title": "Facturación y Pagos en el Sistema SAEw",
    "utterances": [
        "Facturación y Pagos en el Sistema SAEw",
        "¿Cómo se reflejan los pagos y recargos en el SAEw?",
        "Información sobre la facturación en el sistema SAEw",
        "Dudas sobre los valores reflejados en el SAEw",
        "Procedimiento de facturación y pagos en el sistema SAEw",
        "¿Cómo se registran los pagos y recargos en el SAEw?",
        "Detalles sobre el proceso de facturación en el sistema SAEw",
        "Preguntas sobre los valores visualizados en el SAEw",
        "¿Cómo se manejan los pagos y recargos en el sistema SAEw?",
        "Clarificación sobre la facturación en el sistema SAEw",
    ],
    "responses": [
        {
            "type": "text",
            "content": "Si no realizas el pago en las fechas establecidas, el monto adeudado se incluirá en "
                       "la siguiente cuota. En el SAEw, el valor presentado incluirá las cuotas adeudadas "
                       "más un recargo por uso del servicio bancario."
        },
        {
            "type": "action",
            "action": "seleccionar-partes-pago",
            "name": "Cómo Seleccionar el Número de Partes para el Pago"
        },
        {
            "type": "action",
            "action": "dificultades-economicas-cuotas",
            "name": "Qué Hacer en Caso de Dificultades Económicas para Pagar Cuotas"
        }
    ]
}
