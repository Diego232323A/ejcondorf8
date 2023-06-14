from fastapi import FastAPI
from conexion import conexion as bd
from conexion import User
from userModel import UserModel



app=FastAPI(title='Exposicion de Microservicios',description='Construyendo un API',version='1')


@app.get('/')
def index():
    return f'Hola Mundo desde FastApi'
@app.get('/index')
def saludo_desde_index():
    return f'Hola desde /index'

@app.on_event('startup')
def startup():
    if   bd.is_closed():
        print('Inicializando la BD')
        bd.connect()
        #bd.create_tables([User])
@app.on_event('shutdown')
def shutdown():
    if not bd.is_closed():
        print('CERRANDO EL SERVIDOR')
        bd.close()

@app.post('/users/')
def create_user(user:UserModel):
    new_user=User.create(
        username=user.username,
        password=user.password
    )
    print('Usuario Creado')