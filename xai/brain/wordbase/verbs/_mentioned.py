

from xai.brain.wordbase.verbs._mention import _MENTION

#calss header
class _MENTIONED(_MENTION, ):
	def __init__(self,): 
		_MENTION.__init__(self)
		self.name = "MENTIONED"
		self.specie = 'verbs'
		self.basic = "mention"
		self.jsondata = {}
