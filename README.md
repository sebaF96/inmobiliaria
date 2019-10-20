<h1>Inmobiliaria de alquileres</h1>
<h3> Universidad de Mendoza</h3>
<p> Pequeño software de administracion de inmobiliaria de alquileres, con el cual podremos 
agregar, modificar, y llevar cuenta de distintas propiedades clientes y alquileres. 
</p>
<hr>

![MenuPreview](screenshots/preview.png)

<h4> Recursos utilizados: </h3>
<ul>
    <li> <a href="https://www.python.org/">Python3</a> - Lenguaje de programacion
    <li> <a href="https://www.mysql.com/">MySQL</a> - SGBD
    <li> <a href="https://www.sqlalchemy.org/">SQLAlchemy</a> - ORM
    <li> <a href="https://docs.python.org/3/howto/curses.html">curses</a> - Modulo para imprimir menu
</ul>

<hr>
<h4> Diagramas </h4>
<p> Diagrama de entidad relacion </p>

![EER](screenshots/EER.png)

<br>
<p>Diagrama de clases</p>

![CLASES](screenshots/clases.png)


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
Pegar lo siguiente en el archivo y completarlo con las confuguraciones de tu base de datos <br><br>
export DB_CONECTION=Tu_usuario:TuContraseña<br>
export DB_SCHEMA=NombreDeTuBase<br>
export DB_HOST=HostDeTuBase
<br><br>
Guardar el archivo
<li> :wrench: Ejecutar archivo de modelos para generar las tablas y relaciones en la base de datos

```
python3 modelos.py
```
    
<li> Ejecutar archivo main

```
python3 main.py
```


</ul> 

Los pasos que contienen  :wrench: son de configuracion y solo tendras que llevarlos a cabo la primera vez
