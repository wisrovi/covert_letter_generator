# 1) indicamos la imagen base a usar
FROM python:3.8

#Author and Maintainer
LABEL MAINTAINER wisrovi.rodriguez@gmail.com

# 2) creamos una carpeta para alojar los archivos del proyecto
WORKDIR /cover_letter_generator

RUN pip install openai
RUN pip install streamlit

RUN pip freeze

# 6) copiamos la carpeta del codigo y todos sus recursos
COPY src .

CMD ["streamlit", "run", "api.py" ]
