

from xai.brain.wordbase.nouns._personal import _PERSONAL

#calss header
class _PERSONALS(_PERSONAL, ):
	def __init__(self,): 
		_PERSONAL.__init__(self)
		self.name = "PERSONALS"
		self.specie = 'nouns'
		self.basic = "personal"
		self.jsondata = {}
