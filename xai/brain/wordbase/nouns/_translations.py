

from xai.brain.wordbase.nouns._translation import _TRANSLATION

#calss header
class _TRANSLATIONS(_TRANSLATION, ):
	def __init__(self,): 
		_TRANSLATION.__init__(self)
		self.name = "TRANSLATIONS"
		self.specie = 'nouns'
		self.basic = "translation"
		self.jsondata = {}
