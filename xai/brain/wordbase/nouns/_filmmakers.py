

from xai.brain.wordbase.nouns._filmmaker import _FILMMAKER

#calss header
class _FILMMAKERS(_FILMMAKER, ):
	def __init__(self,): 
		_FILMMAKER.__init__(self)
		self.name = "FILMMAKERS"
		self.specie = 'nouns'
		self.basic = "filmmaker"
		self.jsondata = {}
