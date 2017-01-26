

from xai.brain.wordbase.nouns._locale import _LOCALE

#calss header
class _LOCALES(_LOCALE, ):
	def __init__(self,): 
		_LOCALE.__init__(self)
		self.name = "LOCALES"
		self.specie = 'nouns'
		self.basic = "locale"
		self.jsondata = {}
