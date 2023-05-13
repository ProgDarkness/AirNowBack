from cryptography.fernet import Fernet
from dotenv import load_dotenv
import base64
import os

load_dotenv()

def encryptString(encrypted):
  # Genera una clave
  envClave = os.getenv('ENCRYPT_HASH').encode()
  key = base64.b64encode(envClave)
  
  # Crea un objeto Fernet con la clave
  cipher = Fernet(key)
  
  # Encripta un string
  encodeEncrypted = encrypted.encode()
  encrypted_text = cipher.encrypt(encodeEncrypted)
  
  # Retornar texto encriptado
  return encrypted_text

def decryptString(encrypted):
  # Genera una clave
  key = os.getenv('ENCRYPT_HASH')
  
  # Crea un objeto Fernet con la clave
  cipher = Fernet(key)
  
  # Encripta un string
  encrypted_text = cipher.decrypt(encrypted)
  
  # Retornar texto encriptado
  return encrypted_text