

from xai.brain.wordbase.nouns._mention import _MENTION

#calss header
class _MENTIONED(_MENTION, ):
	def __init__(self,): 
		_MENTION.__init__(self)
		self.name = "MENTIONED"
		self.specie = 'nouns'
		self.basic = "mention"
		self.jsondata = {}
