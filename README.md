Como funciona: 

Debes ir a la terminal y ejectuar "python manage.py syncdb" y el te preguntará si deseas crear el administrador web django, le das "yes" y luego ingresas el usuario y la contraseña que usarás para ingresar al administrador.

Luego ejecutas "python manage.py runserver" y si vas a http:localhost:8000 verás los post ingresados en la base de datos y si vas a http:localhost:8000/admin podrás ingresar con el usuario y la contraseña que ingresaste, al administrador de django, para crear nuevos post.