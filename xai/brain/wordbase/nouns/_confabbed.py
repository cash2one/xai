

from xai.brain.wordbase.nouns._confab import _CONFAB

#calss header
class _CONFABBED(_CONFAB, ):
	def __init__(self,): 
		_CONFAB.__init__(self)
		self.name = "CONFABBED"
		self.specie = 'nouns'
		self.basic = "confab"
		self.jsondata = {}
