

from xai.brain.wordbase.nouns._status import _STATUS

#calss header
class _STATUSES(_STATUS, ):
	def __init__(self,): 
		_STATUS.__init__(self)
		self.name = "STATUSES"
		self.specie = 'nouns'
		self.basic = "status"
		self.jsondata = {}
