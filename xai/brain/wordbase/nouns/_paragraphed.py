

from xai.brain.wordbase.nouns._paragraph import _PARAGRAPH

#calss header
class _PARAGRAPHED(_PARAGRAPH, ):
	def __init__(self,): 
		_PARAGRAPH.__init__(self)
		self.name = "PARAGRAPHED"
		self.specie = 'nouns'
		self.basic = "paragraph"
		self.jsondata = {}
