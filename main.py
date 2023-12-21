from flask import Flask
from flask import render_template, request, session, redirect, url_for, flash
from config import DevelopmentConfig
from database import init_db, db_session
from models import Auto, Reserva, Usuario
from flask_wtf import CSRFProtect
from forms import Form_Login
from sqlalchemy import extract
import funciones_extras

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.route('/calendar/<int:id>', methods=['POST'])
def calendario(id):
    fecha_solicitada = funciones_extras.FechaMY(request.form.get('id_post'))
    mes, year = request.form.get('id_post').split('-')
    fecha_actual = funciones_extras.fecha_actual()
    if mes is None or fecha_solicitada.fecha == fecha_actual:
        btn_prev = False
    else:
        btn_prev = True
    reservas = db_session.query(Reserva).filter(Reserva.id_auto == id, extract('month', Reserva.fecha) == mes, extract('year', Reserva.fecha) == year)
    modeloConsultado = db_session.query(Auto.nombre).filter_by(id=id).first()[0]
    reservas=[e.fecha.day for e in reservas]
    return render_template('calendar.html', btn_prev=btn_prev, fecha_actual=fecha_actual, fecha=fecha_solicitada, id=id, modelo_consultado=modeloConsultado, dias_reservados=reservas)


def form_login():
    return Form_Login()


@app.route('/')
def index():
    modelosEnAlquiler = db_session.query(Auto).all()
    return render_template(
        'index.html',
        modelos=modelosEnAlquiler,
        fecha_actual=funciones_extras.fecha_actual(),
        form_login=form_login()
    )
    #return render_template('prueba2.html', fecha_actual=funciones_extras.fecha_actual())

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', form_login=form_login())


@app.route('/quienes_somos')
def quienes_somos():
    cantClientes = 12
    return render_template('quienes_somos.html', cantClientes=cantClientes, form_login=form_login())


@app.route('/login', methods=['POST'])
def login():
    form_login = Form_Login(request.form)
    if request.method == 'POST' and form_login.validate():
        usuario = db_session.query(Usuario).filter(Usuario.username == form_login.usuario.data).first()
        if usuario is not None and usuario.validar_password(form_login.contraseña.data):
            print("User OK")
            session['usuario'] = usuario.username
            return redirect(url_for('index'))



@app.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('usuario')
    return redirect(url_for('index'))


@app.route('/usuarios')
def usuarios():
    return redirect(url_for('index'))


@app.route('/autos')
def autos():
    return redirect(url_for('index'))


@app.route('/reservas')
def reservas():
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run()
