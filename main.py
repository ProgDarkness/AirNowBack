from fastapi import FastAPI, HTTPException, Depends
from uuid import uuid4 as uuid
from models.modelsItems import *
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from database import crud, models, schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Dependencia
def get_db():
  """
  Obtener session de conexion a la base de datos
  """
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


app = FastAPI() 

# Configuración CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
  return {'mensaje': 'Bienvenido a la fastAPI AirNowBack'}

@app.post('/users/', response_model=schemas.User)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
  # Primero se valida si el email existe
  db_user = crud.get_user_by_email(db, email=user.email) 
  
  if db_user:
    raise HTTPException(status_code=400, detail="El email ya existe")
  
  # luego simplemente se retorna lo que envia la funcion de created_user
  return crud.created_user(db=db, user=user) 

@app.get('/users/', response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  # obtener todos los usuarios entre unos limites
  users = crud.get_users(db, skip=skip, limit=limit) 
  return users

@app.get('/users/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
  db_user = crud.get_user(db, user_id=user_id) 
  
  # Valida si el usuario fue encontrado
  if db_user is None:
    raise HTTPException(status_code=404, detail='El usuario no fue encontrado')
  
  # retorna el usuario encontrado
  return db_user

@app.post('/users/{user_id}/items/', response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreated, db: Session = Depends(get_db)):
  # Crea un item para un usuario
  return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get('/items/', response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  # Busca los Items entre dos limites
  items = crud.get_items(db, skip=skip, limit=limit) 
  return items


# old code pruebas fastAPI

""" 
productos = [] 
"""

""" 
@app.get('/productos')
async def obtener_productos():
  return productos

@app.post('/productos')
async def crear_producto(AggProductosArray: list[Producto], tipo_producto_asig: TipoProducto):
  for productoObject in AggProductosArray:
    productoObject.id = str(uuid())
    productoObject.tipo_producto = tipo_producto_asig
    productos.append(productoObject)
  
  return {'mensaje':'Los Productos se han Creado Satisfactoriamente'}

@app.get('/productos/{producto_id}')
async def obtener_producto_por_id(producto_id: str):
  resultado = list(filter(lambda p: p.id == producto_id, productos))
  
  if len(resultado):
    return resultado[0]
  
  raise HTTPException(status_code=404, detail=f"El producto con el ID {producto_id} no fue encontrado")

@app.delete('/productos/{producto_id}')
async def eliminar_producto_por_id(producto_id: str):
  resultado = list(filter(lambda p: p.id == producto_id, productos))
  
  if len(resultado):
    producto = resultado[0]
    productos.remove(producto)
    
    return {'mensaje':f'El producto con ID {producto_id} fue eliminado'}
  
  raise HTTPException(status_code=404, detail=f"El producto con el ID {producto_id} no fue encontrado")

@app.put('/producto/{producto_id}')
async def actualizar_productopor_id(producto_id: str, producto: Producto):
  resultado = list(filter(lambda p: p.id == producto_id, productos))
  
  if len(resultado):
    producto_encontrado = resultado[0]
    producto_encontrado.nombre = producto.nombre
    producto_encontrado.precio_compra = producto.precio_compra
    producto_encontrado.precio_venta = producto.precio_venta
    producto_encontrado.proveedor = producto.proveedor
    
    return producto_encontrado
  
  raise HTTPException(status_code=404, detail=f"El producto con el ID {producto_id} no fue encontrado")

@app.get("/TiposProductos/{tipo_producto}")
async def tipos_producto(tipo_producto: TipoProducto):
  resultado = list(filter(lambda p: p.tipo_producto == tipo_producto, productos))
  
  if len(resultado):
    return resultado
  
  raise HTTPException(status_code=404, detail=f"No se encontraron productos de {tipo_producto}")   
"""