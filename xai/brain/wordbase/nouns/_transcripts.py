

from xai.brain.wordbase.nouns._transcript import _TRANSCRIPT

#calss header
class _TRANSCRIPTS(_TRANSCRIPT, ):
	def __init__(self,): 
		_TRANSCRIPT.__init__(self)
		self.name = "TRANSCRIPTS"
		self.specie = 'nouns'
		self.basic = "transcript"
		self.jsondata = {}
