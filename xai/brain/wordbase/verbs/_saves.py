

from xai.brain.wordbase.verbs._save import _SAVE

#calss header
class _SAVES(_SAVE, ):
	def __init__(self,): 
		_SAVE.__init__(self)
		self.name = "SAVES"
		self.specie = 'verbs'
		self.basic = "save"
		self.jsondata = {}
