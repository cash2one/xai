

from xai.brain.wordbase.nouns._permission import _PERMISSION

#calss header
class _PERMISSIONS(_PERMISSION, ):
	def __init__(self,): 
		_PERMISSION.__init__(self)
		self.name = "PERMISSIONS"
		self.specie = 'nouns'
		self.basic = "permission"
		self.jsondata = {}
