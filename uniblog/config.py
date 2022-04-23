import os

class  Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'secret' # os.getenv('secret_key_ca')
	
	#flack sequrity
	SECURITY_PASSWORD_SALT = 'sault'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'

	#flask wtf - recaptcha
	RECAPTCHA_USE_SSL = False
	RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
	RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
	RECAPTCHA_OPTIONS = {'theme': 'white'}
