

from xai.brain.wordbase.nouns._postcode import _POSTCODE

#calss header
class _POSTCODES(_POSTCODE, ):
	def __init__(self,): 
		_POSTCODE.__init__(self)
		self.name = "POSTCODES"
		self.specie = 'nouns'
		self.basic = "postcode"
		self.jsondata = {}
