from pydantic import BaseModel

class ItemBase(BaseModel):
  """
  Clase Base para item
  """
  title: str
  description: str | None = None
  
class ItemCreated(ItemBase):
  """
  Clase para crear elementos Items
  """
  pass
  
class Item(ItemBase):
  """
  Clase de Item
  """
  id: int
  owner_id: int
  
  class Config:
    orm_mode = True
    
class UserBase(BaseModel):
  """
  Clase Base de User
  """
  email: str
  
class UserCreate(UserBase):
  """
  Clase para Crear Users
  """
  password: str
  
class User(UserBase):
  """
  Clase de User
  """
  id: int
  is_active: bool
  items: list[Item] = []
  
  class Config:
    orm_mode = True
