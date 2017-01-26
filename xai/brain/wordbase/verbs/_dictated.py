

from xai.brain.wordbase.verbs._dictate import _DICTATE

#calss header
class _DICTATED(_DICTATE, ):
	def __init__(self,): 
		_DICTATE.__init__(self)
		self.name = "DICTATED"
		self.specie = 'verbs'
		self.basic = "dictate"
		self.jsondata = {}
