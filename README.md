<h1>Inmobiliaria de alquileres</h1>
<h3> Universidad de Mendoza</h3>
<p> Pequeño software de administracion de inmobiliaria de alquileres, con el cual podremos 
agregar, modificar, y llevar cuenta de distintas propiedades clientes y alquileres. 
</p>
<hr>
<h4> Recursos utilizados: </h3>
<ul>
<li> Python 3
<li> MySQL
<li> SQLAlchemy
<li> curses
</ul>

<hr>
<h4> Diagrama de clases y EER </h4>
<br>
<br>

<hr>

<h4> Como ejecutar? </h4>
<h5> Requisitos </h5>
<ul>
<li> Sistema operativo Linux (por ahora)
<li> Tener instalado Python 3
<li> Tener instalado MySQL
</ul>
<h5> Pasos </h5>
<ul>

<li> :wrench: Crear entorno virtual. Dentro del directorio del proyecto ejecutar
    
```
python3 -m venv .
```

<li> Activar entorno virtual. Dentro del directorio del proyecto ejecutar

```
source bin/activate
```
<li> :wrench: Instalar requerimientos. Con el entorno activado ejecutar

```
pip install -r requeriments.txt
```

<li> :wrench: Crear archivo .env con la configuracion de tu base de datos MySQL

```
vi .env
```
Pegar lo siguiente en el archivo y completarlo con las confuguraciones de tu base de datos <br>
export DB_CONECTION=Usuario:Contraseña
export DB_SCHEMA=NombreDeTuBase
export DB_HOST=hostDeTuBASE
<br>
Guardar el archivo
<li> Ejecutar archivo main

```
python3 main.py
```


</ul> 

Los pasos que contienen  :wrench: son de configuracion y solo tendras que llevarlos a cabo la primera vez
