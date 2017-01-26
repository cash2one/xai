

from xai.brain.wordbase.nouns._overspend import _OVERSPEND

#calss header
class _OVERSPENT(_OVERSPEND, ):
	def __init__(self,): 
		_OVERSPEND.__init__(self)
		self.name = "OVERSPENT"
		self.specie = 'nouns'
		self.basic = "overspend"
		self.jsondata = {}
