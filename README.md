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