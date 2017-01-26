

from xai.brain.wordbase.nouns._person import _PERSON

#calss header
class _PERSONS(_PERSON, ):
	def __init__(self,): 
		_PERSON.__init__(self)
		self.name = "PERSONS"
		self.specie = 'nouns'
		self.basic = "person"
		self.jsondata = {}
