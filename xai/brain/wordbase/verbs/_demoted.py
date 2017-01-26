

from xai.brain.wordbase.verbs._demote import _DEMOTE

#calss header
class _DEMOTED(_DEMOTE, ):
	def __init__(self,): 
		_DEMOTE.__init__(self)
		self.name = "DEMOTED"
		self.specie = 'verbs'
		self.basic = "demote"
		self.jsondata = {}
