este sera el primer intento por hacer esto en Linux asi que tenganme paciencia :)

iniciamos la terminal de WSL y creamos una carpeta llamada wsl-proyects con el comando ``mkdir wsl-proyects`` y luego dentro de esa carpeta hacemos otra llamada ``mkdir todo``
luego arimos el visual studio con el comando ``vcode .`` 

Creamos un archivo HTML dentro llamado "design.html" y agregamos lo siguiente incluyendo el script para llamar a tailwind css

```
<html lang="en">

    <head>

        <meta charset="UTF-8">

        <meta http-equiv="X-UA-Compatible" content="IE=edge">

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Document</title>

    </head>

    <body class="bg-sky-500">

        <nav class="flex items-center justify-between px-4 py-6 text-center bg-gradient-to-r from-cyan-500 to-sky-500">

            <a href="/" class="text-2xl text-white">Tailwind Todo</a>

        </nav>

        <div class="w-4/5 my-6 mx-auto p-2 lg:p-10 bg-white rounded-xl">

            kkkk

        </div>

    </body>

    <script src="https://cdn.tailwindcss.com"></script>

</html>
```

para abrirlo ahora que estamos en Linux un truquito, dentro del vcode le damos click derecho al archivo y le damos en "Mostrar en el explorador"

![[Pasted image 20220629175919.png]]

asi lo abrimos en nuestro navegador y podemos ver como esta y deveria verse asi

![[Pasted image 20220629180006.png]]

luego le ponemos lo siguiente para que tenga el espaciado que queremos

```
    <body class="bg-sky-500">

        <nav class="flex items-center justify-between px-4 py-6 text-center bg-gradient-to-r from-cyan-500 to-sky-500">

            <a href="/" class="text-2xl text-white">Tailwind Todo</a>

        </nav>

        <div class="w-4/5 my-6 mx-auto p-2 lg:p-10 bg-white rounded-xl">

            <form class="flex mb-6 space-x-4">

                <input type="text" name="title" class="title flex-1 px-4 py-3 bg-gray-200 rounded-xl" placeholder="The title"></input>

  

            </form>

        </div>

    </body>
```

debe quedar asi (ojo es input no imput)

![[Pasted image 20220629181426.png]]

ahora le incluimos un baton de agregar asi

```
<button class="p-3 rounded-xl text-white bg-cyan-500 hover:bg-cyan-600">+</button>
```

![[Pasted image 20220629184436.png]]

ahora agregamos el espacio donde ira el titulo y la acción abajo del form así

```
<div class="flex py-3 rounded-xl bg-gray-100">

                <div class="w-4/5">

                    <p class="px-6 text-xs front-medium text-gray-500 uppercase">Title</p>

                </div>

  

                <div class="hidden md:block w-1/5 px-6 text-right">

                    <p class="text-xs font-medium text-gray-500 uppercase">actions</p>

                </div>

            </div>
```

quedando asi

![[Pasted image 20220629184936.png]]

ahora abajo de las acciones ponemos lo siguiente

```  
            <div class="divide-y divide-gray-200" id="todos">

                <article class="flex">

                    <div class="w-4/5 py-3">

                        <p class="px-6 text-xs text-gray-900">The todo title</p>

                    </div>

                </article>

            </div>
```
![[Pasted image 20220629185318.png]]

ahora necesitamos agregarle las acciones asi que agregamos otro div con lo siguiente

```
			<div class="divide-y divide-gray-200" id="todos">

                <article class="flex">

                    <div class="w-4/5 py-3">

                        <p class="px-6 text-xs text-gray-900">The todo title</p>

                    </div>

  

                    <div class="w-1/5 px-6 py-3 flex justify-end space-x-4">

                        <a href="#" class="text-sky-600 hover:text-sky-900">

                            Edit    

                        </a>

                        <a href="#" class="text-sky-600 hover:text-sky-900">

                            Delete

                        </a>

                    </div>

                </article>

            </div>
```
![[Pasted image 20220629191041.png]]

ahora vamos a heroicons.com y buscamos unos buenos SVG para ponerlos como botones

![[Pasted image 20220629192653.png]]

ahora necesitamos crear nuestro entorno virtual, pero como es en Ubuntu no es igual que como lo hacemos en PowerShell, asi que me fui a esta pagina donde lo explican todo https://atareao.es/como/entorno-virtual-en-python-como-y-para-que/

Y guiandome en la pagina entonces vamos a la terminal ye scrivimos este comando
``kei_kusanagi_99@CORTANA:~/wsl-proyects/todo$ sudo apt install python-venv``
esto ya que estamos empezando en ubuntu y tenemos que crear un entorno virtual, con esto instalamos venv para crearlos, ahora ya instalado le damos el comando 
``python3 -m venv env`` siendo env la carpeta  y nombre de nuestro entorno
luego para activarlo escribimos ``source env/bin/activate``

ya activado nuestro entorno le damos ``pip install django``  para poder empezar ahora si a crear nuestra app de django 
![[Pasted image 20220630130542.png]]

le damos ``django-admin startproject django_tailwind_todo`` para crear nuestro proyecto y  ``django-admin startapp todo`` para crear nuestra app
![[Pasted image 20220630194718.png]]


hago un parentesis aqui para enseñar como tube que crear una clave SSH para poder hacer commit en github

segui esto para crear una SSH key
https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

y esto pa agregarla
https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
```
kei_kusanagi_99@CORTANA:~/wsl-proyects/todo$ ssh-keygen -t ed25519 -C kei_kusanagi@outlook.com
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/kei_kusanagi_99/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/kei_kusanagi_99/.ssh/id_ed25519
Your public key has been saved in /home/kei_kusanagi_99/.ssh/id_ed25519.pub
The key fingerprint is:
********************************************** ************@*********.***

The key's randomart image is:
+--[ED25519 256]--+
|B+.  .o.         |
|=ooo o. .        |
|+++.*. o         |
|=oo+.oE          |
|=. +o.. S        |
|*.+.o  . .       |
|=B.*    .        |
|=.X.             |
|o+.o.            |
+----[SHA256]-----+
kei_kusanagi_99@CORTANA:~/wsl-proyects/todo$
```

crei que eso que decia your key fingerprin era la clave y nop, la clave esta guardada en el archivo que termina en .pub
![[Pasted image 20220630192953.png]]

le di mostrar archivos en visual studio y me fui a la carpeta que decia alli y abri el archivo .pub en el block de notas

![[Pasted image 20220630192650.png]]
![[Pasted image 20220630192810.png]]

ahora ya con esto me dejo hacer el push al repositorio
![[Pasted image 20220630193540.png]]
![[Pasted image 20220630193556.png]]

ahora crearemos un view y lo probaremos
asi que en ``/django_tailwind_todo/todo/views.py`` ponemos esto 
```
from django.shortcuts import render

  

def todos(request):

    return render(request, 'todo/todos.html')
```

luego copiamos todo lo que hicimos en la plantilla design.html y creamos una carpeta y un archivo en la app de /todo/templates/todo/todos.html 

![[Pasted image 20220630195305.png]]

ahora como en cada proyecto de Django tenemos que ir a nuestro archivo de urls.py y declarar su path

```
from django.contrib import admin

from django.urls import path

  

from todo.views import todos

  

urlpatterns = [

    path('', todos, name='todos'),

    path('admin/', admin.site.urls),

]
```

solo nos falta declarar nuestra app en nuestro settings.py
![[Pasted image 20220630200143.png]]
listo ahora le damos nuestro amado `` python manage.py runserver`` 

![[Pasted image 20220630202028.png]]

que bonito, ahora crearemos una vista y agregaremos sus tareas

vamos a /todo/models.py y creamos nuestro modelo
```
from django.db import models

  

class Todo(models.Model):

    title = models.CharField(max_length=255)

    is_done = models.BooleanField(default=False)
```
paramos nuestro servidor y hacemos las migraciones

![[Pasted image 20220630212443.png]]

entonces regresamos a nuestro archivo views.py e implementamos esta función

``` 
from django.shortcuts import render

from django.views.decorators.http import require_http_methods

  

from .models import Todo

  

def todos(request):

    return render(request, 'todo/todos.html')

  

@require_http_methods(['POST'])

def add_todo(request):

    todo = None

    title = request.POST.get('title', '')

  

    if title:

        todo = Todo.objects.create(title=title)

  

    return render(request, 'todo/partials/todo.html', {'todo': todo})
```

ahora vamos a urls.py y agregamos ese path que acabamos de poner (el de partials)

```
from django.contrib import admin

from django.urls import path

  

from todo.views import todos, add_todo

  

urlpatterns = [

    path('', todos, name='todos'),

    path('add-todo/' add_todo, name='add_todo'),

    path('admin/', admin.site.urls),

]
```
creamos una nueva carpeta dentro de /templates/todo llamada /partials y dentro creamos un archivo llamado todo.html
![[Pasted image 20220630211339.png]]

vamos a nuestro archivo todos.html y cortamos todo lo que es `<article>` ... `</article>` y lo pegamos en este nuevo archivo y corremos nuestro servidor

![[Pasted image 20220630212234.png]]

ahora vamos a nuestro archivo todos.html y agregamos esto a form y hasta abajo el script siguiente

```
...

<form
	class="flex mb-6 space-x-4"

	hx-post="/add-todo/"

	hx-target="#todos"

	hx-swap="afterend"

>

...

    <script src="https://unpkg.com/htmx.org@1.6.1"></script>

    <script>

        document.body.addEventListener('htmx:configRequest', (event) => {

            event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';

        });

    </script>

...

```


y probamos agregando una tarea por hacer

![[Pasted image 20220630221810.png]]


bien, ahora que ya podemos agregar tareas debemos verlas, para esto vamos a views.py y agregamos esto a la funcion

```
...

def todos(request):

    todos = Todo.objects.all()

    return render(request, 'todo/todos.html', {'todos': todos})
...
```

con esto estamos asignando todos los objetos del modelo Todo a un objeto llamado todos y luego lo pasamos como contexto en el return, ahora vamos a nuestro témplate todos.html y agregamos esto
```
            <div class="divide-y divide-gray-200" id="todos">

                {% for todo in todos %}

                    {% include 'todo/partials/todo.html' %}

                {% endfor %}

            </div>
```

ahora le damos actualizar y tadaaaaaaan
![[Pasted image 20220701125053.png]]

pero aqui aun nos muestra el hard code "the todo title" entonces cambiaremos eso en la plantilla todo.html

```
<article class="flex">

    <div class="w-4/5 py-3">

        <p class="px-6 text-xs text-gray-900">{{ todo.title }}</p>

    </div>
```

![[Pasted image 20220701125345.png]]

ahora quitaremos eso molestod e que creamos una nueva tarea y se queda el titulo alli con el siguiente script en en la plantilla todos.html abajo del otro script que pusimo

```
...

        document.body.addEventListener('htmx:afterRequest', (event) => {

            document.querySelector("input.title").value = '';

        });

...
```
![[Pasted image 20220701131438.png]]

ahora solo tenemos que poner un boton para marcar si una tarea ya esta lista ais que vamos a nuestra plantilla  todo.html y agregamos esto

```
 <a href="#" class="text-sky-600 hover:text-sky-900">

	Done

 </a>
```

ahora vamos a views.py y le ponemos la funcionalidad update

```
@require_http_methods(['PUT'])

def update_todo(request, pk):

    todo = Todo.objects.get(pk=pk)

    todo.is_done = True

    todo.save()

    return render(request, 'todo/partials/todo.html', {'todo': todo})
```

y por ultimo lo agregamos a nuestro urls.py

```
path('update/<int:pk>/', update_todo, name='update_todo'),
```

ahora todo en el back end esta listo, ahora vamos con el front a la pagina todo.html
```
<form

    hx-put="/update/{{ todo.id }}/"

    hx-target="this"

    hx-swap="outerHTML"

>

    <article class="flex">

        <div class="w-4/5 py-3">

            <p class="px-6 text-xs text-gray-900">{{ todo.title }}</p>

        </div>

  

        <div class="w-1/5 px-6 py-3 flex justify-end space-x-4">

            {% if not todo.is_done %}

                <button class="text-sky-600 hover:text-sky-900">

                    Done

                </button>

            {% endif %}

            <a href="#" class="text-sky-600 hover:text-sky-900">

                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">

                    <path stroke-linecap="round" stroke-linejoin="round" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />

                </svg>Edit

            </a>

            <a href="#" class="text-sky-600 hover:text-sky-900">

                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">

                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2M3 12l6.414 6.414a2 2 0 001.414.586H19a2 2 0 002-2V7a2 2 0 00-2-2h-8.172a2 2 0 00-1.414.586L3 12z" />

                </svg>Delete

            </a>

        </div>

    </article>

</form>
```
ahora nos sale la leyenda de Done y si le damos clic queremos ponerle un fondo verde para marcar que ya esta terminado
![[Pasted image 20220701133729.png]]

vamos a todo.html otra ves y modificamos el "article"

```
    <article class="flex {% if todo.is_done %} bg-green-200 {% endif %}">

        <div class="w-4/5 py-3">

            <p class="px-6 text-xs text-gray-900">{{ todo.title }}</p>

        </div>
```
![[Pasted image 20220701134101.png]]

ahora implementaremos la función de borrar tareas, asi que vamos a views.py y agregamos la siguiente función 

```
from django.http.response import HttpResponse

...

@require_http_methods('DELETE'])

def delete_todo(request, pk):

    todo = Todo.objects.get(pk=pk)

    todo.delete()

  

    return Httpresponse()
```

ahora vamos a urls.py y agregamos su path

```
from django.contrib import admin

from django.urls import path

  

from todo.views import todos, add_todo, update_todo, delete_todo

  

urlpatterns = [

    path('', todos, name='todos'),

    path('add-todo/', add_todo, name='add_todo'),

    path('update/<int:pk>/', update_todo, name='update_todo'),

    path('delete/<int:pk>/', delete_todo, name='delete_todo'),

    path('admin/', admin.site.urls),

]
```

ahora vamos con el front end para darle esta funcionalidad a nuestro botón de delete en todo.html en la parte del botón de borrar

```
 <a
	href="#"

	class="text-sky-600 hover:text-sky-900"

	hx-target="closest form"

	hx-swap="outerHTML swap:1s"

	hx-delete="/delete/{{ todo.id }}/"

 >

	<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">

	<path stroke-linecap="round" stroke-linejoin="round" d="M12 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2M3 12l6.414 6.414a2 2 0 001.414.586H19a2 2 0 002-2V7a2 2 0 00-2-2h-8.172a2 2 0 00-1.414.586L3 12z" />

	</svg>Delete
```

listo, cada que le damos en borrar dará un retraso de 1 segundo y borrara la tarea, pero... esto se ve medio feo namas borrarlo y ya, así que vamos a darle un estilo para que desaparezca, asi que vamos otra ves a todos.html y escribimos

```
...

        <title>Tailwind Todo</title>

  

        <style>

            .htmx-swapping {

                opacity: 0;

                transition: opacity 1s ease-out;

            }

        </style>

    </head>

...
```

y ya solo tenemos que agregar una linea a todo.html justo abajo de la class del boton de borrar

```
...

hx-confirm="Are you sure?"

...
```

ahora al darle al botón delete nos aparecerá una advertencia

![[Pasted image 20220701194457.png]]


ahora pondremos la función de editar, vamos a nuestro todo.html y movemos el form para que este dentro del botón done, justo debajo del if

```
...

 <div class="w-1/5 px-6 py-3 flex justify-end space-x-4">

	{% if not todo.is_done %}

		<form

			hx-put="/update/{{ todo.id }}/"

			hx-target="closest article"

			hx-swap="outerHTML"
		>

			<button class="text-sky-600 hover:text-sky-900">
...
```

ahora nos vamos al principio y creamos esta nueva tarea que se referira al poder editar el titulo dando click en el

```
<article class="flex{% if todo.is_done %} bg-green-300{% endif %}">

    <div class="w-4/5 py-3">

        <p

            class="px-6 text-xs text-gray-900"

            hx-get="/edit/{{ todo.id }}/"

            hx-target="this"

            hx-swap="outerHTML"

        >

            {{ todo.title }}

        </p>

    </div>

...
```

si probamos esto ahora nos dará error así que vamos a views.py y creamos la siguiente función

```
@require_http_methods(['GET', 'POST'])

def edit_todo(request, pk):

    todo = Todo.objects.get(pk=pk)

  

    if request.method == 'POST':

        todo.title = request.POST.get('title', '')

        todo.save()

  

        return render(request, 'todo/partials/todo.html', {'todo': todo})

    return render(request, 'todo/partials/edit.html', {'todo': todo})
```

ahora solo falta crear nuestra plantilla que acabamos de declarar, esta estará dentro de /todo/templates/todo/partials/edit.html

```
<form

    hx-post="/edit/{{ todo.id }}/"

    hx-target="closest article"

    hx-swap="outerHTML"

    class="flex"

>

    <input class="flex-1 mr-4 px-6 text-xs text-gray-900 border-0" type="text" name="title" value="{{ todo.title }}" autofocus>

  

    <button class="text-sky-600 hover:text-sky-900"><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">

        <path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />

      </svg>Save</button>

</form>
```

ahora vamos a urls.py y ponemos su path

![[Pasted image 20220704180312.png]]

salvamos y listo, ahora cada que demos click en el titulo de una tarea ya sea este terminada o no podremos editarla

![[Pasted image 20220704180457.png]]

