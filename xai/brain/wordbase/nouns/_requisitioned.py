

from xai.brain.wordbase.nouns._requisition import _REQUISITION

#calss header
class _REQUISITIONED(_REQUISITION, ):
	def __init__(self,): 
		_REQUISITION.__init__(self)
		self.name = "REQUISITIONED"
		self.specie = 'nouns'
		self.basic = "requisition"
		self.jsondata = {}
