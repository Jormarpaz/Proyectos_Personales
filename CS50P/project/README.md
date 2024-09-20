# _Crypto Wallet Visualizer_
#### Video Demo:  https://youtu.be/TKUuOjduuio
#### Description:
Crypto Tracker es una aplicación desarrollada en Python que permite a los usuarios realizar un seguimiento en tiempo real de sus inversiones en criptomonedas. A través de una interfaz gráfica amigable, el proyecto proporciona información detallada sobre las criptomonedas que has comprado, incluidos los precios de compra, el valor actual de tus inversiones y las variaciones de precios en distintos intervalos de tiempo (6 horas y 3 horas). Además, la aplicación te permite agregar, eliminar y gestionar diferentes criptomonedas dentro de tu base de datos, así como actualizar los precios automáticamente utilizando la API de Binance.

El proyecto combina una serie de características esenciales para cualquier persona que gestione activos en criptomonedas, como la actualización dinámica de precios en tiempo real, la gestión de múltiples activos con nombres duplicados (mediante sufijos), y la capacidad de vaciar la base de datos si fuera necesario.

***
#### Archivos y Estructura del Proyecto:
-`project.py:` Este archivo contiene la lógica principal del programa, incluyendo las funciones de interacción con la base de datos, obtención de datos a través de la API de Binance, y las operaciones relacionadas con la interfaz gráfica construida usando Tkinter. La función main() inicializa la aplicación, la interfaz y asegura que los precios de las criptomonedas se actualicen correctamente. Además, incluye las funciones siguientes:

    -`agregar_nueva_cripto():` Permite al usuario añadir una nueva criptomoneda a la base de datos.

    -`eliminar_cripto():` Proporciona la funcionalidad para eliminar una criptomoneda específica de la base de datos.

    -`actualizar_precios():` Obtiene los precios actualizados de todas las criptomonedas registradas y actualiza la tabla de valores.

    -`mostrar_comparacion():` Muestra las diferencias en los precios de las criptomonedas a lo largo del tiempo, permitiendo ver ganancias y pérdidas en tiempo real.

Estas y otras funciones aseguran una experiencia fluida al gestionar tus activos.

-`test_project.py:` Contiene las pruebas unitarias que aseguran el correcto funcionamiento de las funciones críticas de la aplicación. Se usan las bibliotecas unittest y mock para simular las respuestas de la API de Binance y verificar que las funciones de obtención de precios y manipulación de datos operen sin problemas. Las pruebas incluidas cubren:

    -`test_agregar_nueva_cripto():` Verifica que una criptomoneda nueva se pueda añadir a la base de datos correctamente.

    -`test_eliminar_cripto():` Confirma que la eliminación de criptomonedas de la base de datos funciona como se espera.

    -`test_obtener_precio_binance():` Prueba la funcionalidad de consulta a la API de Binance para la obtención de precios en tiempo real.

-`requirements.txt:` Lista de dependencias necesarias para ejecutar el proyecto. El archivo incluye paquetes esenciales como requests (para la interacción con la API) y sv_ttk (para la interfaz gráfica con temas oscuros).
***

***
#### Decisiones de Diseño:
Al desarrollar este proyecto, tuve que tomar varias decisiones importantes sobre el diseño:

**Elección del API:** Opté por la API de Binance para obtener datos actualizados sobre los precios de las criptomonedas debido a su fiabilidad y accesibilidad. Esto me permitió implementar la funcionalidad de precios históricos y en tiempo real, un requisito clave para los usuarios que desean analizar el comportamiento de sus inversiones.

**Manejo de Hilos (Threads):** Debido a la naturaleza asincrónica de la obtención de precios desde la API, decidí implementar varias funciones relacionadas con el manejo de precios dentro de hilos separados. Esto asegura que la interfaz gráfica no se congele mientras se esperan las respuestas de la API y mejora la experiencia del usuario. Aunque inicialmente hubo algunos desafíos relacionados con la actualización intermitente de los datos, los solucioné ajustando la lógica de manejo de hilos para mejorar la eficiencia.

**Interfaz gráfica (Tkinter):** El uso de Tkinter para crear una interfaz gráfica intuitiva fue crucial para hacer el proyecto accesible a usuarios no técnicos. La capacidad de visualizar los datos de manera clara, junto con el uso de barras de desplazamiento y tablas dinámicas, asegura que los usuarios puedan navegar y gestionar su portafolio de criptomonedas fácilmente.
***

#### Conclusión:
Crypto Tracker es una solución efectiva para quienes desean monitorear sus inversiones en criptomonedas con actualizaciones en tiempo real y funcionalidades clave de gestión de activos. El uso de hilos para obtener datos y la implementación de pruebas unitarias aseguran que el proyecto funcione de manera eficiente y sin interrupciones. A medida que se extienda el uso de criptomonedas, herramientas como esta serán esenciales para quienes buscan maximizar sus inversiones.
