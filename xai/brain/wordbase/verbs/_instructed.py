

from xai.brain.wordbase.verbs._instruct import _INSTRUCT

#calss header
class _INSTRUCTED(_INSTRUCT, ):
	def __init__(self,): 
		_INSTRUCT.__init__(self)
		self.name = "INSTRUCTED"
		self.specie = 'verbs'
		self.basic = "instruct"
		self.jsondata = {}
