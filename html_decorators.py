def div(func):
    def new_function(*args, **kwargs):
        hypertext = '<div>'+ func(*args, **kwargs) +'</div>'
        return hypertext
    return new_function


def article(func):
    def new_function(*args, **kwargs):
        hypertext = '<article>'+ func(*args, **kwargs) +'</article>'
        return hypertext
    return new_function


def p(func):
    def new_function(*args, **kwargs):
        hypertext = '<p>'+ func(*args, **kwargs) +'</p>'
        return hypertext
    return new_function


# Here you must apply the decorators, uncomment this later


# @p
# @div
@article
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
