# old code de pruebas de fastAPI

""" 

from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Producto(BaseModel):
  id: Optional[str]
  nombre: str
  precio_compra: float
  precio_venta: float
  proveedor: str
  tipo_producto: Optional[str]
  
class TipoProducto(str, Enum):
  tecnologico = "Tech"
  moviliario = "House"
  decoracion = "Decoration" 

"""
  