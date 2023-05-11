from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uuid
from models.modelsItems import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
  
productos = []

@app.get('/')
async def index():
  return {'mensaje': 'Bienvenido a la fastAPI'}

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