

from xai.brain.wordbase.nouns._user import _USER

#calss header
class _USERS(_USER, ):
	def __init__(self,): 
		_USER.__init__(self)
		self.name = "USERS"
		self.specie = 'nouns'
		self.basic = "user"
		self.jsondata = {}
