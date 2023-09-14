### Install Django

1. Instalar la libreria desde pip

    pip install Django

2. Crear el proyecto:

    django-admin startproject <miproyecto> .  #Linux - mac
    django-admin.exe startproject <miproyecto> .  #win

3. se crea el proyecto dentro de la carpeta donde me encuentro. 

4. Puedo probar y ver mi nuevo proyecto asi:

    python manage.py runserver

5. Me crea el server con le URL para acceder al sitio 

6. Si apaceren pendientes migraciones. Ejecuto el comando:

    python manage.py migrate

7. Ya podemos comprobar que no aparecen actualizaciones.



### Django templating

1. Crear folder "/templates" dentro de proyecto

2. En el "settings.py" se configura rutas para que se usen desde el proyecto asi:

3. Importo la libreria 

    import os

4. Configuro la variable global "SETTINGS_PATH" asi:

    SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))

5. Configuro la ruta del template, asi:    

    - - TEMPLATES
        "DIRS": [ os.path.join(SETTINGS_PATH, 'templates'),],

6. Vamos a llamar nuestro primer template.

7. [[ ENTENDIMIENTO DE TEORIA EL PATRON MVT ]]

8. inicio por crear la ruta. en "urls.py", agrego:

    path("inicio/", inicio),

9. Creo la vista a nivel del proyecto en "views.py", si el archivo no existe se debe crear.

10. Dentro de "views.py" inserto el codigo:

    from django.shortcuts import render

    def inicio(request):
        """Retorna gestion pagina de inicio"""
        return render(request,"pages/inicio.html",{})

11. En "urls.py" debo instanciar la clase que renderiza el Template, Como en este caso estamos 
    construyendo el template desde el mismo proyecto, se instancia con el (.), asi:
   
    from .views import inicio

12. Ahora creo mi archivo HTML en la carpeta que especifique. Coloco algo de HTML para ver que es mi pagina.


#### AHORA, SE CREARA EL HEADER Y EL FOOTER PARA LAS PAGINAS, RESPONDIENDO CON LA JERARQUIA DE TEMPLATES:


13. [[ ENTENDIMIENTO DE LA JERARQUIA DE TEMPLATES ]]

14. Creamos los subfolders dentro de la carpeta "/templates" entre ellos "/layouts"

15. Dentro de "layouts.html" creamos el archivo "base.html"



CRAR UAURIO
min 16,56