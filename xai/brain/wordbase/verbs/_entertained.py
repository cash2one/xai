

from xai.brain.wordbase.verbs._entertain import _ENTERTAIN

#calss header
class _ENTERTAINED(_ENTERTAIN, ):
	def __init__(self,): 
		_ENTERTAIN.__init__(self)
		self.name = "ENTERTAINED"
		self.specie = 'verbs'
		self.basic = "entertain"
		self.jsondata = {}
