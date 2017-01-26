

from xai.brain.wordbase.nouns._eyewitness import _EYEWITNESS

#calss header
class _EYEWITNESSES(_EYEWITNESS, ):
	def __init__(self,): 
		_EYEWITNESS.__init__(self)
		self.name = "EYEWITNESSES"
		self.specie = 'nouns'
		self.basic = "eyewitness"
		self.jsondata = {}
