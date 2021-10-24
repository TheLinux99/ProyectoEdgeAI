# ProyectoEdgeAI
Este repositorio contiene los archivos necesarios para el proyecto 2 del curso de Taller de Sistemas Embebidos, 2do semetre, 2021.
El proyecto consiste en la toma de imagenes con una camara para luego procesarlas y determinar las emociones mediante el rostro de las personas.
El procesamiento se da en una raspberry pi 2 con una aplicacion de Python que utiliza Tensorflow lite y opencv
## Estructura del repositorio
1. Comunication: Contiene los archivos requeridos para la transmision de datos procesados desde la raspberry pi al usuario.
2. Conf: Contiene archivos de configuracion para sintetizar correctamente la imgen mediante el uso de Yocto Project. 
   - El archivo bblayers.conf tiene agregadas las capas necesarias
   ```
   BBLAYERS ?= " \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-poky \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-yocto-bsp \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-openembedded/meta-oe \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-openembedded/meta-python \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-openembedded/meta-networking \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-openembedded/meta-multimedia \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-raspberrypi \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-tensorflow-lite \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-ia \
   /home/linux/Documents/Git-Repositorys/Yocto/poky/meta-FastEmotRecognition \
   "
   ``` 
   - En el local.conf estan las configuraciones para utilizar los paquetes de las capas y la target machine definida como raspberry pi 2.
   ```
   MACHINE ??= "raspberrypi2"
   ```
   ```
   IMAGE_INSTALL_append += " python3-tensorflow-lite"
   IMAGE_INSTALL_append += " python3-pip"
   CORE_IMAGE_EXTRA_INSTALL += " python3"
   CORE_IMAGE_EXTRA_INSTALL += " opencv"
   CORE_IMAGE_EXTRA_INSTALL += " FastEmotRecognition"
   ```
3. Instalation Files: Contiene dos scripts que son los unicos que instala Yocto Project en la imagen de la raspberry pi, estos scripts tiene la funcion de descargar los modulos de Python restantes y la aplicacion escogida para el analisis de emociones.
4. meta-FastEmotRecognition: Capa creada para incluir la receta que permite a Yocto Project instalar los scripts mencionados en el punto anterior en la imagen de la raspberry pi.
5. poky: La carpeta poky corresponde a la estructura minima necesaria para que yocto project pueda sintetizar la imagen requerida, las capas que contiene son:
   - [meta-openembedded](https://github.com/openembedded/meta-openembedded)
   - [meta-raspberripi](https://github.com/agherzan/meta-raspberrypi)
   - [meta-tensorflow-lite](https://github.com/NobuoTsukamoto/meta-tensorflow-lite)
6. Python: Contiene la aplicacion selecionada de Python junto a los archivos necesarios para su ejecucion, la aplicacion original se puede encontrar en este [repositorio](https://github.com/hfahrudin/FastEmotRecognition), sin embargo, aplicamos unos cambios para que utilice unicamente tensorflow lite.
7. deploys.txt: Contiene links a las imagenes sintetizadas listas para descargarlas en la raspberry pi.
