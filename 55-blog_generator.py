import openai
from decouple import config

openai.api_key = config('API_KEY')


# Definimos una función, con un parámetro que será el tema utilizado para generar el párrafo.

def generate_blog(paragraph_topic):
    response = openai.Completion.create(  # Para almacenar la respuesta generada por la salida de la llamada al método en nuestro m´dulo openai.
        # Parámetro del modelo tendrá en cuenta el modelo que queremos usar. Este es el mejor de todos.
        model='text-davinci-002',
        # Son las instrucciones principales para GPT-3. Este parámetro se llevará a nuestro argumento.
        prompt='Write a paragraph about the following topic. ' + paragraph_topic,
        max_tokens=400,  # Esto decide cuánto tiempo va a durar la respuesta.
        temperature=0.3  # Determina la aleatoriedad de una respuesta. Una temperatura más alta producirá una respuesta más creativa, mientras que una temperatura más baja producirá una respuesta más bien definida.
    )
    # Para acceder al valor en el campo de text.
    retrieve_blog = response.choices[0].text
    # Devolvemos la variable que contiene el párrafo que acabamos de sacar del diccionario.
    return retrieve_blog


# Para usar como un valor booleano para el siguiente bucle.
keep_writing = True

while keep_writing:  # Aceptará una entrada del usuario.
    # ¿Escribir un párrafo? Y por sí, cualquier otra cosa por no.
    answer = input('Write a paragraph? Y for yes, anything else for no. ')
    if (answer == 'Y'):
        # ¿De qué debería hablar este párrafo?
        paragraph_topic = input('What should this paragraph talk about? ')
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False   # Detenemos el bucle.
