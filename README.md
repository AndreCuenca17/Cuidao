
# Instrucciones para configurar el proyecto

### 1. Abrir el proyecto en Visual Studio Code
   - Abre la carpeta **"Proyecto-Cuidao"** en Visual Studio Code.

### 2. Eliminar la máquina virtual existente
   - Dentro de la carpeta **"flask-backend"**, elimina la carpeta **"venv"** si ya existe.
### 3. Crear una nueva máquina virtual
   - En la terminal de Visual Studio Code, ejecuta uno de los siguientes comandos para crear un entorno virtual:
     ```
     py -m venv venv
     # o
     python -m venv venv
     ```

### 4. Activar la máquina virtual
   - **En Windows**, navega a la carpeta **Scripts** dentro de **venv** y ejecuta:
     ```
     .\venv\Scripts\activate
     ```
### 5. Instalar dependencias desde `requirements.txt`
   - Una vez que la máquina virtual esté activa, instala las dependencias necesarias para el proyecto:
     ```
     pip install -r requirements.txt
     ```

### 6. Correr el servidor Flask
   - Navega a la carpeta **"flask-backend"** y ejecuta el servidor Flask:
     ```
     py run.py
     # o
     python run.py
     ```

### 7. Correr el servidor de React
   - En la carpeta **"react-frontend"**, ejecuta el siguiente comando para iniciar el servidor de desarrollo:
     ```bash
     npm start
     ```
### 8. Acceder a la página web localmente
   - Después de ejecutar los pasos anteriores, la aplicación debería abrirse automáticamente en tu navegador. Si no es así, abre **http://localhost:3000** en tu navegador.

### Consideraciones
   - Crear la carpeta **templates** dentro de **app** para el almacenamiento de los mapas
   - Crear el archivo **.env** dentro de flask-backend y escribir las variables de entorno
     ```
     API_KEY = *****
     MODEL_NAME = *****
     ``` 
   - Crear la carpeta **cache** dentro de flask-backend
   - Para ejecutar **npm start**, asegúrate de tener **Node.js** instalado. Si aún no lo tienes, puedes descargarlo desde [Node.js](https://nodejs.org/en/).
   - Instalar las dependencias de Node.js dentro de **react-frontend** mediante el comando
     ```
     npm install
     ``` 
   - Verifica que **npm** esté instalado correctamente ejecutando:
     ```
     npm --version
     ```