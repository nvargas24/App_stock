# app_stock

## Autores
Ing. Calderón, Diego  
Sr. Vargas, Nahuel

## Tabla de Contenidos
- [Introducción](#introducción)
- [Aclaraciones](#aclaraciones)
- [Versión Tkinter](#versión_tkinter)
    - [Ejecución](#ejecución)
    - [Uso](#uso)
- [Versión QTDesigner](#versión_qtdesigner)
    - [Ejecución](#ejecución)
    - [Uso](#uso)
- [Versión KivyMD](#versión_kivymd)
    - [Ejecución](#ejecución)
    - [Uso](#uso)
- [Licencia](#licencia)

## Introducción
En este repositorio se contará con la app de control de stock diseñada para el cierre de la diplomatura en Python, 
llevado a cabo en la Universidad Tecnologica Nacional regional Buenos Aire E-Learning.

Se implementa una interfaz de usuario utilizando el patron MVC con una base de datos SQLite. 

## Aclaraciones
En dicha diplomatura consto de realizar un app por etapas, es decir, poner en practica la escalabilidad de un proyecto.
Por eso, se realizo la app con: #Tkinter #QtDesigner #KivyMD.

Las 3 versiones fueron realizadas en un principio en gitlab, en un único proyecto con distintas ramas, al pasar a github (por falta de experiencia),
sólo quedaron resgitrados los commits en la version en Tkinter.

## Versión_Tkinter
### Ejecución
```
pip install peewee
pip install pandas
pip install matplotlib
```

```
python tkinter/controlador.py
```
### Uso
La app al ejecutarse se tendrá disponible esta única ventana.    
![](Imagenes/tkinter1.jpg)
+ **Formulario**: Sección que permite al usuario cargar los datos, estos cuenta con verificación de campos según la accion a realizar.
+ **CRUD**: Acciones a realizar con los datos cargados en formularios.
+ **Recarga de base datos**: Consulta __todos__ los datos en la base datos y carga en la tabla.
+ **Tabla de base de datos**: Se cargan todos o algún datos consultado a la base de datos.

Al ejecutar la app, el usuario puede ingresar los siguientes parametros:  
+ *Nombre*
+ *Cantidad*
+ *Precio*
+ *Descripción*  

En la sección CRUD, puede interactuar con la base de datos:  
+ ***Agregar artículo***: se tomarán todos los campos se sección **Formulario**. Estos serán cargados en la base de datos.  
+ ***Eliminar artículo***: se toma sólo el campo **Nombre** y se buscará en la base datos, si existe se elimina de la base
de datos, si no existe no se realiza nada.  
+ ***Modificar artículo***: se toman todos los campos, verificando primero por **Nombre** si existe el artículo. Si existe
se procede a modificar los demas parametros cargados en el fomulario para dicho artículo.  
+ ***Consultar stock***: se toma solo el campo **Nombre**, y se busca en la base de datos. Si existe se muestra en la tabla
con todos sus parametros actuales.

*Dependiendo de la acción a realizar se verifica que los campos involucrados no esten vacios y cumpla el regex (sólo numero/letras)*

Aparte de las acciones disponibles en la sección CRUD, se cuenta con la opción ***Ver Catálogo completo***. El cual lee y 
muestra todos los datos disponibles en la base de datos en la tabla y en un gráfico de tortas, realizado con Matplotlib.

***Toda acción realizada será notificada por medio de popup y por terminal implementando decoradores***

## Versión_QTDesigner
### Ejecución
```
python qtdesigner/controlador.py
```
La app al ejecutarse abrirá la ventana principal.    
![](Imagenes/qt_main.jpg)

### Uso
Dependiendo de la opción seleccionada se abre una ventana distinta las cuales son:  
+ ***Agregar artículo***  
    ![](Imagenes/qt_agregar.jpg)
+ ***Eliminar artículo***  
    ![](Imagenes/qt_eliminar.jpg)
+ ***Modificar artículo***  
    ![](Imagenes/qt_modificar.jpg)
+ ***Consultar stock***  
    ![](Imagenes/qt_consulta.jpg)  

## Versión_KivyMD
### Ejecución
```
python kivymd/controlador.py
```

### Uso

## Licencia



