from sqlalchemy.orm import Session
from . import models, schemas
from utils.cryptography import encryptString, decryptString

def get_user(db: Session, user_id: int):
  """
  obtener usuarios de la base de datos
  
  parametro db: sesion de la base de datos
  parametro user_id: id del usuario en base de datos
  """
  return db.query(models.User).filter(models.User.id == user_id).first()
  
def get_user_by_email(db: Session, email: str):
  """
  Consultar usuario por email
  
  parametro db: sesion de la base de datos
  parametro email: email del usuario
  """
  return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
  """
  Consultar un limite usuarios
  
  parametro db: sesion de la base de datos
  parametro skip: es para marcar desde donde va a comenzar a consultar los usuarios
  parametro limit: es para marcar hasta donde va a consultar los usuarios
  
  return lista de usuarios
  """
  return db.query(models.User).offset(skip).limit(limit).all()

def created_user(db: Session, user: schemas.UserCreate):
  """
  Crear un usuario
  
  parametro db: sesion de la base de datos
  parametro user: usuario a crear
  
  return usuario creado
  """
  fake_hashed_password = encryptString(user.password)
  db_user = models.User(email = user.email, hashed_password=fake_hashed_password)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

def get_items(db: Session, skip: int = 0, limit: int = 100):
  """
  Consultar un limite de items
  
  parametro db: sesion de la base de datos
  parametro skip: es para marcar desde donde va a comenzar a consultar los items
  parametro limit: es para marcar hasta donde va a consultar los items
  
  return lista de items
  """
  return db.query(models.Item).offset(skip).limit(limit).all()

def create_user_item(db: Session, item: schemas.ItemCreated, user_id: int):
  """
  Crear un item
  
  parametro db: sesion de la base de datos
  parametro item: item a crear
  parametro user_id: id del usuario que le pertenece el item
  
  return item creado
  """
  db_item = models.Item(**item.dict(), owner_id=user_id)
  db.add(db_item)
  db.commit()
  db.refresh(db_item)
  return db_item
