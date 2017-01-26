

from xai.brain.wordbase.verbs._delete import _DELETE

#calss header
class _DELETING(_DELETE, ):
	def __init__(self,): 
		_DELETE.__init__(self)
		self.name = "DELETING"
		self.specie = 'verbs'
		self.basic = "delete"
		self.jsondata = {}
