# Automatización y pruebas de la aplicación web Urban Routes

Este proyecto consiste en el desarrollo de un sistema de automatización de pruebas para la plataforma Urban Routes, aplicación de transporte que permite a los usuarios solicitar taxis, seleccionar tarifas y gestionar pagos de manera eficiente.

El objetivo principal del proyecto es validar el correcto funcionamiento de las funcionalidades clave de la plataforma a través de pruebas automatizadas con Selenium Web Driver y Python.

Estas pruebas garantizan que los usuarios puedan:

1) Seleccionar una ruta de origen y destino.
2) Escoger la tarifa de confort.
3) Ingresar y verificar su número de teléfono
4) Agregar métodos de pago y tarjetas de crédito
5) Enviar mensaje al conductor
6) Solicitar accesorios adicionales como mantas o helado
7) Confirmar la asignación de un conductor y la visualización del modal de viaje.

TECNOLOGÍAS UTILIZADAS
1) Lenguaje de programación: Python
2) Framework de pruebas: pytest y unittest
3) Automatización web: Selenium WebDriver
4) Manejo de localizadores: XPath, ID, CSS Selectors
5) Registro de logs y depuración: logging. WebDriver Logs
6) Gestión de esperas dinámicas: WebDriverWait y expected_condictions

ESTRUCTURA DEL PROYECTO

El código está organizado en los siguientes archivos:

1) main.py

a) Contiene los casos de prueba automatizados
b) Configura el entorno de pruebas con Selenium
c) Ejecuta validaciones sobre las funcionalidades clave

2) data.py

a) Almacena datos de prueba como direcciones, números de teléfono y tarjetas.

3) locators.py
a) Define los localizadores de elementos en la interfaz usuario.

4) sms.py
a) Gestiona la recuperación de códigos de verificación por SMS durante la autenticación

COMO EJECUTAR LAS PRUEBAS

Para ejecutar las pruebas de automatización, hacer lo siguiente:

1) Ejecutar pruebas con pytest


