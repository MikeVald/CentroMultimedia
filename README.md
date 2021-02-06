# CentroMultimedia
Proyecto Final para la materia de Fundamentos de Sistemas Embebidos

### Instrucciones de configuración
Este sistema funciona en sistema opertivo Raspbian con versión de Kernel: 5.4.\
Se recomienda 2 GB de memoria RAM Y 15 GB de disco duro. 

### Instrucciones de instalación
Es indispensable tener instalado el reproductor VLC, se puede obtener en la siguiente página: [VLC](https://www.videolan.org/vlc/index.es-MX.html)\
La versión de VLC es 3.0.12 \
Se recomienda instalar el reproductor VLC con la configuracion tradicional indicada en el instalador de la aplicación. \
Una vez descargado e instalado, el reproductor VLC, debemos tener instalado el software python e instalar las siguientes utilerías: \
Se debe correr en la terminal, en modo administrador, los siguientes comandos: \
`sudo apt-get update`\
`sudo apt-get install python3.6`\
`sudo apt-get install python-tk`\
`sudo pip install pil`\
`pip install python-vlc`

### Instrucciones de operación
Para que el archivo funcione, debemos de ejecutar en la carpeta donde descarguemos el archivo py con el siguiente comando:\
`python CentroMultimedia.py `\
En la pantalla principal de la interfaz, podemos seleccionar nuestra plataforma de interés o podemos hacer click en el modo de reproducción local. \
Si se selecciona la reproducción local debemos de asegurarnos de meter el contenido multimedia en una carpeta que debemos crear en el escritorio llamada `PFE`.

### Copyright e información de licencia 
Copyright 2021 Equipo 8

Por la presente se concede permiso, libre de cargos, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), a utilizar el Software sin restricción, incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar, y/o vender copias del Software, y a permitir a las personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:\
\
El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.
EL SOFTWARE SE PROPORCIONA "COMO ESTA", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO PARTICULAR E INCUMPLIMIENTO. EN NINGÚN CASO LOS AUTORES O PROPIETARIOS DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, DERIVADAS DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O SU USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.

### Contacto
> fenixdark64@hotmail.com \
> francisco.g.rosas.p@gmail.com \
> michael.valdezz@yahoo.com

### Bugs conocidos
*Si a las imágenes o videos, en reproducción, se aprieta el botón next el VLC se va para atrás y debes manualmente volver a traerlo al frente.
*Cuando aprietas el botón de pausa realmente no se pone pausa, es un stop porque si le pones play de nuevo, se reinicia toda la playlist.

### Solución de problemas
* Reiniciar el programa.

### Créditos y agradecimientos
Agredimientos a todo el equipo que diseñó, codificó e implementó las soluciones que se tomaron. Este proyeco fue realizado especialmente para la materia de Fundamentos de Sistemas Embebidos como parte de la evalución del Proyecto Final.

## Versión 1.0
