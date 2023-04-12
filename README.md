# Aplicación de Mensajería

Esta aplicación consiste en dos programas que permiten envío y recepción de mensajes
entre dos máquinas; una asumiendo el papel de "servidor" y la otra la de "cliente".

## Instalación

Se debe clonar el repositorio en la carpeta deseada, usando el comando:

`git clone https://github.com/Grupo12-INF331-PdS/tarea-1-validacion-y-verificacion.git`

La clonación debe ser realizada en ambas máquinas.

## ¿Cómo usar?

Ambas máquinas deben estar conectadas a la misma red WiFi.

Ejecutar en la máquina que cumplirá el rol de servidor:
`python server.py`
La máquina entrará en espera de un cliente.

La otra máquina será el cliente:
`python cliente.py`
Esperar a que se establezca la conexión y ¡Listo!, ambas máquinas podrán interactuar.

El cliente debe ser el primero en enviar un mensaje, de esta forma se entrará en una especie de mensajería tipo "correos electrónicos" entre las máquinas.

Para finalizar la conexión, escribir "/exit" en el espacio de mensajería:
`>> /exit`
Si una de las dos máquinas finaliza la sesión, la otra automáticamente se desconectará y terminará el programa.

## ¿Cómo contribuir?

¡Aceptamos cualquier tipo de aporte! Somos un equipo pequeño en busca de experiencia,
por lo que tu sabiduría es bienvenida. Abre un Pull Request si deseas aportarnos con
alguna mejora que hayamos pasado por alto.

## Licencia

El siguiente enlace te llevará a la licencia del [MIT](/LICENSE).
