

from xai.brain.wordbase.nouns._database import _DATABASE

#calss header
class _DATABASES(_DATABASE, ):
	def __init__(self,): 
		_DATABASE.__init__(self)
		self.name = "DATABASES"
		self.specie = 'nouns'
		self.basic = "database"
		self.jsondata = {}
