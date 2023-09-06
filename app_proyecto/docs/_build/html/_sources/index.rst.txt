.. ControlDeStock documentation master file, created by
   sphinx-quickstart on Fri Mar  3 18:13:35 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenidos a la documentación de Control de Stock
==================================================

**Control de Stock** es una app que permite al usuario realizar la inspección del stock de una tienda de 
electrónica, donde, mediante los distintos botones, podrá ingresar un nuevo componente, eliminarlo,
modificarlo, o verificar la disponibilidad del mismo (consultando ya sea por nombre y/o descripción). 
Según sea la ventana en la que se encuentre, se mostrará un mensaje de manera de avisar si la acción fue realizada exitosamente o cuál fue el error.

El usuario también podrá visualizar, en la ventana principal, un gráfico de torta con los componentes ingresados hasta el momento, el cual se actualizará
tras presionar el botón de "Consultar Stock".

La app además ejecuta un servidor al que cualquier cliente podrá conectarse, y consultar el stock total de artículos disponibles, 
el de un componente en particular o cerrar la conexión cuando lo desee.

.. note::

   Esta aplicación se encuentra aún en desarrollo.


.. toctree::
   :maxdepth: 7 
   :caption: Contenidos:

   controlador
   modelo
   validar
   vista
   observador
   cliente
   servidor

Indices y tablas
================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
