import hashlib

class CryptographicHash:
	"""
		Esta Clase tiene como proposito principal la encriptacion
		de datos. Actualmente solo cuenta con un metodo, pero la 
		idea es agregar metodos conforme a la necesidad.
	"""

	def __init__(self, encryptType): 
		self.encryptType = encryptType

	def encrypt(self, data):
		"""
			Encriptamos el dato enviado y retornamos el resultado
			IMPORTANTE: data=b''
		"""	
		return hashlib.new(self.encryptType, bytes(data, 'utf-8')).hexdigest()
