# Proyecto de Gestión de Usuarios

Este proyecto Python proporciona funcionalidades básicas para la gestión de usuarios, incluyendo registro, inicio de sesión y cierre de sesión.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso Básico](#uso)
- [Funcionalidades](#funcionalidades)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Instalación

Puedes instalar el paquete usando pip. Asegúrate de tener Python y pip instalados en tu sistema.


pip install proyecto_login

## Uso Básico - Ejemplo de registro e inicio de sesión de usuarios


from proyecto_login import GestorUsuarios

    # Crear una instancia del Gestor de Usuarios
gestor = GestorUsuarios()

    # Registrar usuarios
gestor.registrar_usuario("usuario1", "password123")
gestor.registrar_usuario("usuario2", "secreto456")

    # Iniciar sesión
gestor.iniciar_sesion("usuario1", "password123")

    # Cerrar sesión
gestor.cerrar_sesion("usuario1")

## Funcionalidades

- **Registrar Usuario**: Permite registrar nuevos usuarios con nombre de usuario y contraseña.
- **Iniciar Sesión**: Verifica las credenciales de un usuario y permite iniciar sesión si son correctas.
- **Cerrar Sesión**: Finaliza la sesión de un usuario activo.

## Contribuir

¡Las contribuciones son bienvenidas! Si tienes sugerencias o encuentras algún problema, por favor abre un issue en [GitHub].

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, revisa el archivo LICENSE.