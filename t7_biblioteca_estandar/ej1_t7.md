# ¿Cuál es la diferencia entre os.path.join() y os.path.abspath?

 - os.path.join() es una función que se utiliza para unir uno o más componentes de ruta en una sola ruta. Maneja inteligentemente los separadores de ruta según el sistema operativo. Por ejemplo, os.path.join('folder', 'file.txt') devuelve 'folder/file.txt' en sistemas basados en Unix y 'folder\\file.txt' en Windows.

- os.path.abspath es una función que devuelve la ruta absoluta de un archivo o directorio dado. Proporciona la ruta completa y canónica, que incluye el directorio completo desde el directorio raíz


# ¿Cuál es el propósito del módulo os? Da ejemplos de su uso.

Provee una manera versátil de usar funcionalidades dependientes del sistema operativo, como interactuar con el sistema de archivos y ejecutar comandos.

1 - Cambiar el directorio de trabajo:

```python
import os
os.chdir('/ruta/a/directorio')
```
2 - Listar archivos en un directorio:

```python
import os
archivos = os.listdir('.')
```


# ¿Cuál es el propósito del módulo logging? ¿Cómo se usa?

El módulo ‘logging’ de Python es un módulo de la biblioteca estándar que permite registrar eventos y mensajes en un programa de forma flexible y extensible.

Para usar el módulo logging, primero necesitas importarlo:

```python
import logging
```
Luego necesitas crear un objeto logger:

```python
logger = logging.getLogger('mi_logger')
```

Entonces puedes usar el objeto logger para registrar mensajes:

```python
logger.debug('Este es un mensaje de depuración.')
logger.info('Este es un mensaje informativo.')
logger.warning('Este es un mensaje de advertencia.')
logger.error('Este es un mensaje de error.')
logger.critical('Este es un mensaje crítico.')
```