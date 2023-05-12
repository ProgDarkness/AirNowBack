# AirNowBack
API para backend de la aplicacion movil de vuelos de aerolineas, esta desarrollado con Python v3.11.3,
se usara el Framework de FastAPI con el servidor uvicorn, bajo los estandares de creacion de APIs

# CREATED

# Crear Ambiente Virtual
```sh
python -m venv venv
```

# Iniciar Ambiente Virtual en PowerShell
```sh
./venv/Scripts/Activate.ps1
```
Importante este comando es para trabajar sobre el ambiente, 
siempre debe estar el nombre del ambiente antes de la ubicacion 
del promp sea CMD o sea PowerShell

# Instalar Paquetes de FastAPI
```sh
pip install fastapi 
```
Este recurso solo se ejecutara una vez al crear el ambiente.

# Instalar Servidor 
```sh 
pip install "uvicorn[standard]"
```
Este recurso solo se ejecutara una vez al crear el ambiente.

# Instalar PAquetes de Conexion a base de datos
```sh 
pip install sqlalchemy
```

# Iniciar Servidor
```sh 
uvicorn main:app --reload
```
Este comando es el estandar para subir el servicio y poder probar el API,
usar siempre dentro del ambiente virtual. 
El servicio se puede consultar en http://localhost:8000 
La documentacion de la API se puede ver en http://localhost:8000/docs