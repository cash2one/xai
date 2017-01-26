

from xai.brain.wordbase.nouns._fault import _FAULT

#calss header
class _FAULTED(_FAULT, ):
	def __init__(self,): 
		_FAULT.__init__(self)
		self.name = "FAULTED"
		self.specie = 'nouns'
		self.basic = "fault"
		self.jsondata = {}
