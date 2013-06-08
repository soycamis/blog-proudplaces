Requisitos:

Django 1.5.1
Python Image Library 

Como funciona: 

Vas a la terminal e instalas la libreria de imágenes de python con el siguiente comando: pip install pil

Ejectuas "python manage.py syncdb" y el te preguntará si deseas crear el administrador web django, le das "yes" y luego ingresas el usuario y la contraseña que usarás para ingresar al administrador.

Luego ejecutas "python manage.py runserver" y si vas a http:localhost:8000 verás los post ingresados en la base de datos y si vas a http:localhost:8000/admin podrás ingresar con el usuario y la contraseña que ingresaste, al administrador de django, para crear nuevos post.