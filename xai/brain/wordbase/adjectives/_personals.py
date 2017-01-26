

from xai.brain.wordbase.adjectives._personal import _PERSONAL

#calss header
class _PERSONALS(_PERSONAL, ):
	def __init__(self,): 
		_PERSONAL.__init__(self)
		self.name = "PERSONALS"
		self.specie = 'adjectives'
		self.basic = "personal"
		self.jsondata = {}
