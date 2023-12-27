import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() # En la creación de la instancia de FastAPI, necesitas agregar paréntesis ()
                # después de FastAPI para inicializarla correctamente: app = FastAPI().

@app.get('/')
def get_root():
    return [1, 2, 3]

@app.get('/contact', response_class=HTMLResponse) # Para que sea de tipo HTML.
def get_contact():
    return '''
        <h1>¡Hola mundo. Soy una página!<h1>
        <p>¡Y yo soy un párrafo!<p>
    
'''


def run():
    store.get_categories()

if __name__ == '__main__' :
    run()