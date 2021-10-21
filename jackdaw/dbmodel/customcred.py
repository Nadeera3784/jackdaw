from aiosmb.commons.connection.target import SMBTarget
from msldap.commons.credential import MSLDAPCredential, LDAPAuthProtocol
from msldap.commons.target import MSLDAPTarget
from minikerberos.common.creds import KerberosCredential, KerberosSecretType
from . import Basemodel
import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from jackdaw.dbmodel.utils.serializer import Serializer

from aiosmb.commons.connection.credential import SMBCredential, SMBAuthProtocol, SMBCredentialsSecretType

class CustomCred(Basemodel, Serializer):
	__tablename__ = 'customcreds'
	
	id = Column(Integer, primary_key=True)
	ownerid = Column(String, index=True)
	domain = Column(String)
	username = Column(String)
	stype = Column(String) #password/nt/rc4/aes/etc...
	secret = Column(String)
	description = Column(String, index=True)

	def __init__(self, username, stype, secret, description, domain = None, ownerid=None):
		self.ownerid = ownerid
		self.domain   = domain
		self.username = username
		self.stype = stype
		self.secret = secret
		self.description = description
	
	def get_smb_cred(self, authtype:SMBAuthProtocol, target:SMBTarget = None, settings:dict = None):
		stype = None
		dbstype = self.stype.upper()
		if dbstype in ['PW', 'PASSWORD', 'PASS']:
			stype = SMBCredentialsSecretType.PASSWORD
		elif dbstype in ['AES', 'AES128', 'AES256']:
			stype = SMBCredentialsSecretType.AES
		elif dbstype in ['KEYTAB']:
			stype = SMBCredentialsSecretType.KEYTAB
		elif dbstype in ['KIRBI']:
			stype = SMBCredentialsSecretType.KIRBI
		
		if authtype == SMBAuthProtocol.NTLM:	
			if dbstype in ['RC4', 'NT']:
				stype = SMBCredentialsSecretType.NT

		if stype is None:
			raise Exception('Couldnt figure out correct stype for customcred!')
		
		return SMBCredential(
			username = self.username, 
			domain = self.domain, 
			secret = self.secret, 
			secret_type = stype, 
			authentication_type = authtype, 
			settings = settings, 
			target = target
		)
	
	def get_ldap_cred(self, authtype:LDAPAuthProtocol, target:MSLDAPTarget = None, settings:dict = None):
		return MSLDAPCredential(
			domain= self.domain, 
			username= self.username, 
			password = self.secret, 
			auth_method = authtype,
			settings = settings, 
			etypes = None, 
			encrypt = False
		)
	
	def get_kerberos_cred(self):
		stype = None
		dbstype = self.stype.upper()
		if dbstype in ['PW', 'PASSWORD', 'PASS']:
			kc = KerberosCredential()
			kc.domain = self.domain
			kc.username = self.username
			kc.add_secret(KerberosSecretType.PASSWORD, self.secret)
			return kc
		elif dbstype in ['RC4', 'NT']:
			kc = KerberosCredential()
			kc.domain = self.domain
			kc.username = self.username
			kc.add_secret(KerberosSecretType.RC4, self.secret)
			return kc
		elif dbstype in ['AES', 'AES128', 'AES256']:
			kc = KerberosCredential()
			kc.domain = self.domain
			kc.username = self.username
			kc.add_secret(KerberosSecretType.AES, self.secret)
			return kc
		elif dbstype in ['KEYTAB']:
			kc = KerberosCredential.from_keytab(self.secret)
			kc.domain = self.domain
			kc.username = self.username
			return kc
		elif dbstype in ['KIRBI']:
			kc = KerberosCredential.from_kirbi(self.secret)
			return kc
		
		if stype is None:
			raise Exception('Couldnt figure out correct stype for customcred!')
