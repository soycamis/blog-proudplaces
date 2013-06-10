# Blog Proudplaces

Este blog se ha desarrollado con la idea de centralizar las notificaciones e informar a la comunidad de todo lo que está pasando y las novedades del proyecto colaborativo Proudplaces.

## Requisitos

* Python
* SQlite
* Django 1.5.1
* Python Image Library

## Como empezar

Si no tienen Python Image Library pueden instalarlo con el siguiente comando:

	pip install pil

Para crear la base de datos y activar el administrador tenemos que ejecutar el comando:

	python manage.py syncdb
	
Nos preguntará si deseamos crear el administrador web Django, aceptamos escribiendo "yes" y luego nos preguntara el usuario y la contraseña que usaremos para acceder al administrador.

Para iniciar la aplicación:
	
	python manage.py runserver
	

La aplicación se iniciará en http://localhost:8000 y el administrador se encuentra http:localhost:8000/admin, el usuario y contraseña son los que creaste anteriormente.