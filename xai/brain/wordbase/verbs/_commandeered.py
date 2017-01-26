

from xai.brain.wordbase.verbs._commandeer import _COMMANDEER

#calss header
class _COMMANDEERED(_COMMANDEER, ):
	def __init__(self,): 
		_COMMANDEER.__init__(self)
		self.name = "COMMANDEERED"
		self.specie = 'verbs'
		self.basic = "commandeer"
		self.jsondata = {}
