from flask import Flask, render_template_string, request

app = Flask(__name__)

ESTILOS = '''
<style>
    body { font-family: 'Segoe UI', sans-serif; background-color: #115566; margin: 0; padding: 0; color: #56992F; }
    .nav { background-color: #348565; padding: 15px 30px; display: flex; justify-content: space-between; }
    .nav a { color: white; text-decoration: none; margin-left: 20px; font-weight: bold; }
    .contenedor { max-width: 600px; margin: 50px auto; padding: 20px; }
    .caja { background-color: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .boton { background-color: #F49C92; color: white; padding: 12px 20px; border: none; border-radius: 5px; text-decoration: none; display: inline-block; cursor: pointer; }
    input, textarea { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; margin-top: 5px; margin-bottom: 15px; box-sizing: border-box; }
</style>
'''
BASE_HTML = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contacto Escuela</title>
    ''' + ESTILOS + '''
</head>
<body>
    <div class="nav">
        <div style="color: white; font-weight: bold;">Escuela</div>
        <div>
            <a href="/">Inicio</a>
            <a href="/contacto">Contacto</a>
        </div>
    </div>
    <div class="contenedor">
        {{ contenido | safe }}
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    html_inicio = '''
    <div class="caja" style="text-align: center;">
        <h1>¡Bienvenido/a!</h1>
        <p>¿Tienes dudas o sugerencias?</p><br>
        <a href="/contacto" class="boton">Ir al formulario de contacto</a>
    </div>
    '''
    return render_template_string(BASE_HTML, contenido=html_inicio)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        
        html_exito = f'''
        <div class="caja">
            <h1 style="color: #22c55e; text-align: center;">✔ ¡Mensaje enviado!</h1><br>
            <p><strong>Nombre:</strong> {nombre}</p>
            <p><strong>Correo:</strong> {correo}</p>
            <p><strong>Mensaje:</strong> {mensaje}</p><br><br>
            <div style="text-align: center;">
                <a href="/" class="boton">Volver al inicio</a>
            </div>
        </div>
        '''
        return render_template_string(BASE_HTML, contenido=html_exito)

    html_formulario = '''
    <div class="caja">
        <h1>Formulario de contacto</h1><br>
        <form action="/contacto" method="POST">
            <label>Nombre:</label>
            <input type="text" name="nombre" placeholder="Tu nombre" required>
            
            <label>Correo electrónico:</label>
            <input type="email" name="correo" placeholder="Tu correo" required>
            
            <label>Mensaje:</label>
            <textarea name="mensaje" rows="5" placeholder="Escribe tu mensaje" required></textarea>
            
            <button type="submit" class="boton">Enviar</button>
        </form>
    </div>
    '''
    return render_template_string(BASE_HTML, contenido=html_formulario)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
