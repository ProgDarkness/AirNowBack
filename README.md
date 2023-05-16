# AirNowBack

API para backend de la aplicacion movil de vuelos de aerolineas, esta desarrollado con Python v3.11.3,
se usara el Framework de FastAPI con el servidor uvicorn, bajo los estandares de creacion de APIs

# CREATED

# Crear Ambiente Virtual

```sh
python -m venv venv
```

# Comando para ejecucion de scripts en PowerShell

```sh
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

Este comando es para poder ejecutar el ambiente virtual.

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

# Instalar Paquetes de Conexion a base de datos

```sh
pip install sqlalchemy
```

# Instalar Paquetes de Encriptacion de password

```sh
pip install cryptography
```

# Iniciar Servidor

```sh
uvicorn main:app --reload --host <IPlocalMachine> --port 8080
```

Este comando es el estandar para subir el servicio y poder probar el API,
usar siempre dentro del ambiente virtual.
El servicio se puede consultar en http://<IPlocalMachine>:8080
La documentacion de la API se puede ver en http://<IPlocalMachine>:8080/docs
