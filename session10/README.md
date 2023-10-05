### CAP 1: Install Django

1. Instalar la libreria desde pip
    ```
    pip install Django
    ```

2. Crear el proyecto:
    ```
    django-admin startproject <miproyecto> .  #Linux - mac
    python -m django startproject <miproyecto> .  #win
    ```

3. se crea el proyecto dentro de la carpeta donde me encuentro. 

4. Puedo probar y ver mi nuevo proyecto asi:
    ```
    python manage.py runserver
    ```

5. Me crea el server con le URL para acceder al sitio 

6. Si apaceren pendientes migraciones. Ejecuto el comando:
    ```
    python manage.py migrate
    ```

7. Ya podemos comprobar que no aparecen actualizaciones.

> Conclusión: Django instalado en nuestro entorno de desarrollo.

### CAP 2: Django templating

1. Crear folder "/templates" dentro de proyecto

2. En el "settings.py" se configura rutas para que se usen desde el proyecto asi:

3. Importo la libreria 
    ```
    import os
    ```

4. Configuro la variable global "SETTINGS_PATH" asi:

    ```
    SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
    ```

5. Configuro la ruta del template, asi:    
    ```
    - - TEMPLATES
        "DIRS": [ os.path.join(SETTINGS_PATH, 'templates'),],
    ```
6. Vamos a llamar nuestro primer template.

7. **[[ ENTENDIMIENTO DE TEORIA EL PATRON MVT ]]**

8. inicio por crear la ruta. en "urls.py", agrego:
    ```
    path("inicio/", inicio),
    ```
9. Creo la vista a nivel del proyecto en "views.py", si el archivo no existe se debe crear.

10. Dentro de "views.py" inserto el codigo:
    ```
    from django.shortcuts import render

    def inicio(request):
        """Retorna gestion pagina de inicio"""
        return render(request,"pages/inicio.html",{})
    ```
11. En "urls.py" debo instanciar la clase que renderiza el Template, Como en este caso estamos 
    construyendo el template desde el mismo proyecto, se instancia con el (.), asi:
    ```
    from .views import inicio
    ```
12. Ahora creo mi archivo HTML en la carpeta que especifique. Coloco algo de HTML para ver que es mi pagina.


> Conclusión: Se tiene en "templates/pages" las paginas de cada seccion de forma convencional SIN jerarquia de templates.*


#### CAP3: AHORA, JERARQUIA DE TEMPLATES:

1. **[[ ENTENDIMIENTO DE LA JERARQUIA DE TEMPLATES ]]**

2. Creamos los subfolders dentro de la carpeta "/templates" entre ellos "/layouts" y "/includes"

3. Vamos a crear la plantilla del "template", Dentro de "layouts.html" creamos el archivo "base.html"

4. Basicamente dentro de "base.html" vamos a crear 3 espacios dinamicos:
    ```
    {% block title %} {% endblock %}
    ```
    ```
    {% include "includes/header.html" %}
    ```
    ```
    {% block content %}  {% endblock %}
    ```

    ::: warning
    *block, se utiliza para definir áreas reemplazables en una plantilla base que las plantillas hijas pueden sobrescribir. Está relacionado con la herencia de plantillas.
    include, se utiliza para insertar el contenido de una plantilla dentro de otra, permitiendo la reutilización de fragmentos de código quen no cambian.*
    :::

5. Crear dentro de "/templates/includes/" el archivo "header.html".

6. Ahora, se trabaja en la plantilla hija. inicialmente se trabajara desde "/pages/inicio1.html"

7. Primero, se define que esta plantilla depende una plantilla padre, asi:
    ```
    {% extends "layouts/base.html" %}
    ```
8. Luego definimos los "block" con la informacion dinamica, asi
    ```
    {% block title %} << titulo de la pagina >> {% endblock %}
    {% block content %} << contenido de la pagina >> {% endblock %}
    ```

#### CAP4: INTEGRANDO CSS Y JS

0. Hacer el ajuste de las carpetas del proyecto. Por buenas practicas deben quedar como en **(Django - Folders Structure Guide Lines)** y entonces se debe ajustar la ruta del "templates" asi:

    ```
    "DIRS": [os.path.join(BASE_DIR, 'templates'),],
    ```

1. Primero configuramos el acceso a los archivos "static".

2. En el archico 'settings.py', configuramos asi:

    ```
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (os.path.join(BASE_DIR, '<miproyecto>/static'), )
    ```
3. En cada template donde voy a hacer uso de archivos estaticos, debo configurar la variable asi;

    ```
    {% load static %}
    ```

4. La forma de llamar los archivos desde 'static/' es :

    ```
    <link href="{% static 'css/styles.css' %}" rel="stylesheet" />
    <img class="profile-img" src="{% static 'assets/profile.png' %}" alt="..." />
    ```

[[CHALLENGE]]: Incluir una hoja de css custom y una de js custom 


5. Para efectos del ejercicio en clase. Vamos a integrar un template que existe en el mercado, basado en Boostrap. [Template Free proyecto](https://startbootstrap.com/theme/personal)

6. Descargamos el template y vamos a explorar su codigo HTML.

7. ...Waiting...

8. Entendamos un poco [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

9. Algunos ejemplos: [Bootstrap-Examples](https://getbootstrap.com/docs/4.0/examples/)

10. ...Waiting...

11. Tomamos de ejemplo una de las paginas del "template". EJ:index.html

12. Separamos sus componentes en: Header, Footer, Content.

13. Y los cluimos en los bloques del "Template" que corresponda.

#### CAP5: PRIMERA APP - PROYECTOS

1. Vamos a crear un super usuario para acceder al administrador, asi:

2. En el terminal con el siguiente comando :

    ```
    python manage.py createsuperuser
    ```

3. Luego creamos nuestra aplicacion para el proyectos, En este caso es la app de proyectos, asi:

4. ir a la carpeta "apps/" y dentro de esta ejecutar el comando:

    ```
    django-admin startapp <nombre-app>
    ```

5. Aparecera dentro de nuestra carpeta "Aplicaciones/<nueva-app>/" con los archivos de python.

6. Agregamos la nueva app al archivo de configuracion del proyecto, asi:
 
    ```
    "Aplicaciones.proyectos",
    ```

7. Ahora en el archivo "apps.py" de mi aplicacion, configuramos el nombre de la aplicacion, asi:

    ```
    class ProyectosConfig(AppConfig):
        default_auto_field = "django.db.models.BigAutoField"
        name = "Aplicaciones.proyectos"
    ```

8. Dentro de nuesta aplicacion, vamos al archivo "models.py", alli, declaramos la estructura que 
   tendra el objeto Proyecto en la Base de datos. Por ahora vamos a definir 4 campos (Codigo, nombre, descripcion y publish).

    ```
    class Proyecto(models.Model):
        codigo = models.CharField(primary_key=True,max_length=4)
        nombre = models.CharField(max_length=90)
        descripcion = models.CharField( max_length=2000 )
        publish = models.BooleanField(default=True)
    ```


9. Ahora vamos al archivo "admin.py", aqui le decimos Django que este modelo se va a administrar 
   desde su interfaz. asi:

    ```
   from .models import Proyecto  

   admin.site.register(Proyecto)
    
    ```

10. Ahora en la consola ejecutamos el comando, 
    ```
    python manage.py migrate
    ```
    Si no presenta errores, ejecutamos el siguiente:
    ```
    python manage.py makemigrations
    ```  

    Si el terminal reporta `(You have 1 unapplied migration(s).)`, ejecute en el terminal nuevamente:
    ```
    python manage.py migrate
    ```

11. Ahora, vamos a crear la pagina "proyectos.html" pero desde la nueva Aplicacion "proyectos/templates" 
y no desde el "template" principal.


12. Para ello primero generamos las urls desde "proyectos/urls.py"


``` 
from django.urls import path
from . import views

urlpatterns = [ 
    path("proyectos/", views.proyectos, name="Proyectos"),
]
``` 

y le decimos al archivo de urls del proyecto, que ahora tambien vamos a tener urls dentro de 
una Aplicacion, asi:

```
from django.urls import path, include

+ path("", include('Aplicaciones.proyectos.urls')),  
```

13. Ahora voy a generar la lista de cursos. Dentro de "views.py" de mi Aplicacion, importo el modelo,

```
from .models import Proyecto
```

Genero la consulta por medio del ORM, y lo envio como variable al "template/proyectos.html"

```
def proyectos(request):
    mis_proyectos = Proyecto.objects.all()
    return render(request,"pages/proyectos.html",{"proyectos":mis_proyectos})
```    

14. **[[ ENTENDIMIENTO DE QUE ES UN ORM ]]**

15. Ahora ajusto la plantilla "templates/proyecto.html" para que itere, y muestre los proyectos.

16. **[[ ENTENDIMIENTO DE QUE ES JINJA2 ]]**



#### Resources.
[Template Free proyecto](https://startbootstrap.com/theme/personal)


#### Django - Folders Structur Guide Lines

my_project/
│
├── my_project/                 # Configuración principal del proyecto.
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/                       # Todas las aplicaciones de Django se almacenan aquí.
│   ├── users/                  # Una aplicación para gestionar usuarios.
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── orders/                 # Otra aplicación para gestionar pedidos.
│   │   ... (estructura similar a 'users')
│   │
│   └── ...                     # Otras aplicaciones.
│
├── static/                     # Archivos estáticos globales (CSS, JS, imágenes).
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/ 
│   ├── layouts/                # Plantillas (templates) globales.
│   │   ├── base.html
│   ├── includes/
│   │   ├── header.html
│   │   ├── footer.html
│   ├── pages/
│   │   ├── inicio.html
│   │   ├── resumen.html
│   │   ├── proyectos.html
│
├── media/                      # Archivos subidos por el usuario (Si se necesita).
│
├── .gitignore
├── README.md
├── requirements.txt            # Todas las dependencias del proyecto.
└── manage.py



