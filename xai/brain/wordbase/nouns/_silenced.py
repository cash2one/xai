

from xai.brain.wordbase.nouns._silence import _SILENCE

#calss header
class _SILENCED(_SILENCE, ):
	def __init__(self,): 
		self.name = "SILENCED"
		self.basic = "silence"
		self.jsondata = {}
