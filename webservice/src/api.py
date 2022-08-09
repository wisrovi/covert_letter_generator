import openai as ai
import streamlit as st
import os
import sys

API_KEY = os.environ.get("API_KEY")
if API_KEY is None:
    print("No se encuentra la variable del sistema")
    sys.exit()

print("** Loading API Key")
ai.api_key = API_KEY

st.title("Guía de aplicaciones de trabajo de Wisrovi")
st.markdown("# Cover Letter Generator 🎈")
st.sidebar.markdown("# Cover Letter Generator  🎈")

with st.sidebar:
    model_used = st.selectbox(
        'GPT-3 Model',
        #  ('DaVinci', 'Curie', 'Babbage', 'Ada'))
        ('text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001'))

    if model_used == 'text-davinci-002':
        st.markdown("""[Davinci](https://beta.openai.com/docs/models/davinci) es la familia de modelos más capaz y puede realizar cualquier tarea que la otra
         los modelos pueden realizar y, a menudo, con menos instrucción. Para aplicaciones que requieren mucho
         comprensión del contenido, como resúmenes para una audiencia específica y contenido creativo
          generación, Davinci va a producir los mejores resultados. Estos aumentaron
          Las capacidades requieren más recursos informáticos, por lo que Davinci cuesta más por llamada API y no es tan rápido como los otros modelos..
        """)
        # st.markdown("""
        # Good at:
        #     * Complex intent
        #     * cause and effects
        #     * summarization for audience
        # """)
    elif model_used == 'text-curie-001':
        st.markdown("""[Curie](https://beta.openai.com/docs/models/curie) es extremadamente poderoso, pero muy rápido. Mientras que Davinci es más fuerte cuando
         cuando se trata de analizar texto complicado, Curie es bastante capaz de muchas tareas matizadas como el sentimiento
         clasificación y resumen. Curie también es bastante bueno respondiendo preguntas y realizando
         Preguntas y respuestas y como chatbot de servicio general.
        """)
    elif model_used == 'text-babbage-001':
        st.markdown("""[Babbage](https://beta.openai.com/docs/models/babbage) puede realizar tareas sencillas como una clasificación simple. también es bastante
         capaz cuando se trata de clasificación de búsqueda semántica qué tan bien los documentos coinciden con las consultas de búsqueda.
        """)
    else:
        st.markdown("""[Ada](https://beta.openai.com/docs/models/ada) suele ser el modelo más rápido y puede realizar tareas como analizar texto, dirección
         corrección y ciertos tipos de tareas de clasificación que no requieren demasiados matices.
         el rendimiento de da a menudo se puede mejorar proporcionando más contexto.
        """)
    st.markdown(
        "**Nota:** Las descripciones de los modelos se toman del sitio web [OpenAI](https://beta.openai.com/docs)")

    max_tokens = st.text_input("Número máximo de tokens:", "1949")
    st.markdown(
        "**Nota importante:** A menos que el modelo que esté utilizando sea Davinci, entonces mantenga el número máximo total de fichas < 1950 para evitar que el modelo se rompa. Si está utilizando Davinci, mantenga un máximo de tokens < 3000.")

    st.subheader("Additional Toggles:")
    st.write("¡Cámbielos solo si desea agregar información de parámetros específicos al modelo!")
    temperature = st.text_input("Temperatura: ", "0.99")
    top_p = st.text_input("Top P: ", "1")

with st.form(key='my_form_to_submit'):
    company_name = st.text_input("Nombre empresa: ", "Google")
    role = st.text_input("¿Para qué puesto te postulas? ", "Machine Learning Engineer")
    contact_person = st.text_input("¿A quién estás enviando un correo electrónico? ", "Technical Hiring Manager")
    your_name = st.text_input("¿Cuál es su nombre? ", "Amber Teng")
    personal_exp = st.text_input("tengo experiencia en...",
                                 "natural language processing, fraud detection, statistical modeling, and machine learning algorithms. ")
    job_desc = st.text_input("Estoy emocionado por el trabajo porque...",
                             "this role will allow me to work on technically challenging problems and create impactful solutions while working with an innovative team. ")
    passion = st.text_input("Soy apasionado por...",
                            "solving problems at the intersection of technology and social good.")
    #job_specific = st.text_input("¿Qué te gusta de este trabajo? (Por favor sea breve, una sola oración.) ")
    #specific_fit = st.text_input(
    #    "¿Por qué crees que tu experiencia es adecuada para este puesto? (Por favor sea breve, una sola oración.)")
    submit_button = st.form_submit_button(label='Submit')

prompt = (
        "Write a cover letter to " + contact_person + " "
        + "from " + your_name + " "
        + "for a " + role + " "
        + "job at " + company_name + "."
        + " I have experience in " + personal_exp
        + " I am excited about the job because " + job_desc
        + " I am passionate about " + passion)

if submit_button:
    # The Model
    response = ai.Completion.create(
        engine=model_used,
        # engine="text-davinci-002", # OpenAI has made four text completion engines available, named davinci, ada, babbage and curie. We are using davinci, which is the most capable of the four.
        prompt=prompt,  # The text file we use as input (step 3)
        max_tokens=int(max_tokens),  # how many maximum characters the text will consists of.
        temperature=0.99,
        # temperature=int(temperature), # a number between 0 and 1 that determines how many creative risks the engine takes when generating text.,
        top_p=int(top_p),  # an alternative way to control the originality and creativity of the generated text.
        n=1,  # number of predictions to generate
        frequency_penalty=0.3,
        # a number between 0 and 1. The higher this value the model will make a bigger effort in not repeating itself.
        presence_penalty=0.9
        # a number between 0 and 1. The higher this value the model will make a bigger effort in talking about new topics.
    )

    text = response['choices'][0]['text']
    print("Prompt:", prompt)
    print("Response:", text)

    st.subheader("Cover Letter Prompt")
    st.write(prompt)
    st.subheader("Auto-Generated Cover Letter")
    st.write(text)
    st.download_button(label='Download Cover Letter', file_name='cover_letter.txt', data=text)

    print("Other results:", response)

    with open('cover_letters.txt', 'a') as f:
        f.write(text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("SO started")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
