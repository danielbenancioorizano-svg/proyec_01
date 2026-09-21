import random
import streamlit as st

# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Quiz de Machine Learning",
    page_icon="🤖",
    layout="centered"
)

# ============================================================
# BANCO DE 10 PREGUNTAS
# ============================================================

QUESTION_BANK = [

    {
        "question": "¿Qué es Machine Learning?",
        "options": [
            "Una técnica para que las computadoras aprendan patrones a partir de datos",
            "Un lenguaje de programación",
            "Un tipo de hardware",
            "Un sistema operativo"
        ],
        "answer": "Una técnica para que las computadoras aprendan patrones a partir de datos"
    },

    {
        "question": "¿Cuál es uno de los tipos principales de Machine Learning?",
        "options": [
            "Aprendizaje supervisado",
            "Aprendizaje mecánico",
            "Aprendizaje manual",
            "Aprendizaje estático"
        ],
        "answer": "Aprendizaje supervisado"
    },

    {
        "question": "En el aprendizaje supervisado, ¿qué característica tienen normalmente los datos?",
        "options": [
            "Tienen ejemplos con una respuesta o etiqueta conocida",
            "No contienen ningún dato",
            "Solo contienen imágenes",
            "Siempre son generados por robots"
        ],
        "answer": "Tienen ejemplos con una respuesta o etiqueta conocida"
    },

    {
        "question": "¿Cuál de estos es un ejemplo de aprendizaje no supervisado?",
        "options": [
            "Agrupar clientes según características similares",
            "Predecir el precio de una casa usando precios históricos etiquetados",
            "Clasificar correos como spam usando ejemplos etiquetados",
            "Predecir una nota usando datos con notas conocidas"
        ],
        "answer": "Agrupar clientes según características similares"
    },

    {
        "question": "¿Qué busca hacer la clasificación en Machine Learning?",
        "options": [
            "Asignar datos a categorías o clases",
            "Eliminar todos los datos",
            "Aumentar físicamente la memoria de una computadora",
            "Convertir cualquier dato en una imagen"
        ],
        "answer": "Asignar datos a categorías o clases"
    },

    {
        "question": "¿Qué busca hacer la regresión?",
        "options": [
            "Predecir un valor numérico",
            "Crear únicamente grupos sin etiquetas",
            "Eliminar variables automáticamente",
            "Convertir texto en hardware"
        ],
        "answer": "Predecir un valor numérico"
    },

    {
        "question": "¿Qué es un modelo de Machine Learning?",
        "options": [
            "Una representación aprendida a partir de datos para realizar predicciones o decisiones",
            "Un archivo de música",
            "Una pieza física del computador",
            "Una conexión a Internet"
        ],
        "answer": "Una representación aprendida a partir de datos para realizar predicciones o decisiones"
    },

    {
        "question": "¿Para qué se suele dividir un conjunto de datos en entrenamiento y prueba?",
        "options": [
            "Para entrenar el modelo y luego evaluar su desempeño con datos separados",
            "Para duplicar el tamaño del disco",
            "Para evitar usar algoritmos",
            "Para convertir datos numéricos en imágenes"
        ],
        "answer": "Para entrenar el modelo y luego evaluar su desempeño con datos separados"
    },

    {
        "question": "¿Qué significa que un modelo haga overfitting (sobreajuste)?",
        "options": [
            "Aprende demasiado bien los datos de entrenamiento y puede rendir peor con datos nuevos",
            "No aprende absolutamente nada",
            "Siempre obtiene exactamente 50% de aciertos",
            "No utiliza ningún dato durante el entrenamiento"
        ],
        "answer": "Aprende demasiado bien los datos de entrenamiento y puede rendir peor con datos nuevos"
    },

    {
        "question": "¿Cuál es un ejemplo cotidiano de Machine Learning?",
        "options": [
            "Un sistema que recomienda películas según tus preferencias",
            "Encender una bombilla con un interruptor",
            "Usar una regla para medir una mesa",
            "Escribir un documento en papel"
        ],
        "answer": "Un sistema que recomienda películas según tus preferencias"
    }
]


# ============================================================
# FUNCIÓN PARA CREAR UN NUEVO CUESTIONARIO
# ============================================================

def new_quiz():

    # Seleccionar 5 preguntas aleatorias de las 10
    selected_questions = random.sample(QUESTION_BANK, 5)

    questions = []

    for question in selected_questions:

        # Copiar las alternativas
        options = question["options"].copy()

        # Mezclar alternativas
        random.shuffle(options)

        questions.append({
            "question": question["question"],
            "options": options,
            "answer": question["answer"]
        })

    # Guardar el cuestionario en la sesión
    st.session_state.quiz = questions

    # Reiniciar estado
    st.session_state.submitted = False


# ============================================================
# CREAR PRIMER CUESTIONARIO
# ============================================================

if "quiz" not in st.session_state:
    new_quiz()


# ============================================================
# TÍTULO
# ============================================================

st.title("🤖 Quiz de Machine Learning")

st.write(
    "Pon a prueba tus conocimientos básicos sobre "
    "Machine Learning, sus tipos y conceptos generales."
)

st.info(
    "💡 Cada cuestionario contiene 5 preguntas seleccionadas "
    "aleatoriamente de un banco de 10."
)


# ============================================================
# FORMULARIO DEL QUIZ
# ============================================================

with st.form("quiz_form"):

    for i, question in enumerate(st.session_state.quiz, start=1):

        st.subheader(f"Pregunta {i} de 5")

        st.write(question["question"])

        st.radio(
            "Selecciona una alternativa:",
            question["options"],
            key=f"question_{i}",
            index=None,
            label_visibility="collapsed"
        )

        st.divider()

    submitted = st.form_submit_button(
        "✅ Comprobar respuestas",
        use_container_width=True
    )


# ============================================================
# CALCULAR RESULTADO
# ============================================================

if submitted:

    score = 0

    # Revisar las 5 respuestas
    for i, question in enumerate(st.session_state.quiz, start=1):

        user_answer = st.session_state.get(f"question_{i}")

        if user_answer == question["answer"]:
            score += 1

    # Guardar puntuación
    st.session_state.score = score
    st.session_state.submitted = True

    # ========================================================
    # RESULTADO
    # ========================================================

    st.divider()

    st.header(f"🎯 Resultado: {score}/5")

    # ========================================================
    # SI RESPONDIÓ TODO CORRECTAMENTE
    # ========================================================

    if score == 5:

        st.success(
            "🎉 ¡Excelente! Respondiste correctamente "
            "todas las preguntas."
        )

        # Animación
        st.balloons()

        st.markdown(
            """
            ## 🏆 ¡PERFECTO!

            Has conseguido **5 de 5 respuestas correctas**.

            ¡Demostraste un excelente dominio de los
            conceptos básicos de Machine Learning! 🤖
            """
        )

    # ========================================================
    # SI OBTUVO 3 O 4
    # ========================================================

    elif score >= 3:

        st.warning(
            f"👍 ¡Buen trabajo! Obtuviste {score}/5. "
            "Repasa los conceptos que fallaste."
        )

    # ========================================================
    # SI OBTUVO 0, 1 O 2
    # ========================================================

    else:

        st.error(
            f"📚 Obtuviste {score}/5. "
            "No te preocupes, sigue practicando."
        )


    # ========================================================
    # MOSTRAR CORRECCIONES
    # ========================================================

    st.subheader("📋 Corrección")

    for i, question in enumerate(
        st.session_state.quiz,
        start=1
    ):

        user_answer = st.session_state.get(
            f"question_{i}"
        )

        if user_answer == question["answer"]:

            st.success(
                f"Pregunta {i}: ✅ Correcta"
            )

        else:

            st.error(
                f"Pregunta {i}: ❌ Incorrecta"
            )

            st.write(
                f"**Respuesta correcta:** "
                f"{question['answer']}"
            )


# ============================================================
# BOTÓN NUEVO CUESTIONARIO
# ============================================================

st.divider()

if st.button(
    "🔄 Generar nuevo cuestionario",
    use_container_width=True
):

    # Eliminar respuestas anteriores
    for i in range(1, 6):

        if f"question_{i}" in st.session_state:

            del st.session_state[f"question_{i}"]

    # Crear nuevas preguntas
    new_quiz()

    # Recargar aplicación
    st.rerun()


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.caption(
    "🤖 Quiz educativo de Machine Learning | "
    "5 preguntas aleatorias de un banco de 10"
)
