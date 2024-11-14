# Documentación

## Instrucciones para ejecutar el servidor y el cliente

### Ejecutar el servidor

1. Abre una terminal.
2. Navega al directorio donde se encuentra el archivo `server.py`.
3. Ejecuta el siguiente comando:
    ```sh
    python server.py
    ```
4. El servidor comenzará a escuchar en `localhost:5000`.

### Ejecutar el cliente

1. Abre otra terminal.
2. Navega al directorio donde se encuentra el archivo `client.py`.
3. Ejecuta el siguiente comando:
    ```sh
    python client.py
    ```
4. Ingresa los mensajes que deseas enviar al servidor para que sean **transformados** en mayúsculas.

## Instrucciones para realizar pruebas manuales

1. Prueba - Enviar un mensaje de texto:

    Siguiendo los pasos anteriores, ingresa un mensaje en la terminal del cliente y observa la respuesta del servidor. Por ejemplo:
    ```sh
    Hola, mundo
    ```
    El servidor debería responder con:
    ```sh
    HOLA, MUNDO
    ```

2. Prueba - Enviar un mensaje para cerrar la conexión:

    Ingresa el mensaje `DESCONEXION` en la terminal del cliente y observa la respuesta tanto del servidor como del cliente. Por ejemplo:

    El servidor debería responder con:
    ```sh
    Servidor cierra la conexión con el cliente...
    ```

    El cliente debería responder con:
    ```sh
    Cerrando la conexión...
    ```
    Y la conexión estaría cerrada en ambos extremos.