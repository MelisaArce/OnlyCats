from flask import Blueprint, redirect, render_template, request, url_for
from jinja2 import TemplateNotFound

blueprint = Blueprint('home_blueprint', __name__, url_prefix='')


@blueprint.route('/')
def route_default():
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/index')
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
def route_template(template: str):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound: #poner los html de error
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:
        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
    
@blueprint.route('/sign_in', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Procesar los datos del formulario
        cuidador_nombre = request.form['cuidador nombre']
        mich_nombre = request.form['michi nombre']
        email = request.form['email']
        password=request.form['password']
        # Realizar cualquier operación que desees con los datos recibidos
        # Por ejemplo, puedes almacenarlos en una base de datos o hacer cálculos con ellos.
       # return f"¡Hola {nombre}! Tu correo es {email}."
    # Si el método es GET (primera visita al formulario), simplemente renderiza el formulario.
    return render_template('/page_sign_up.html')

@blueprint.route('/sign_up', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Procesar los datos del formulario
        apellido = request.form['apellido']
        nombre = request.form['nombre']
        email = request.form['email']
        # Realizar cualquier operación que desees con los datos recibidos
        # Por ejemplo, puedes almacenarlos en una base de datos o hacer cálculos con ellos.
        return f"¡Hola {nombre}! Tu correo es {email}."
    # Si el método es GET (primera visita al formulario), simplemente renderiza el formulario.
    return render_template('/page_sign_up.html')