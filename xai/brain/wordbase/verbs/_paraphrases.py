

from xai.brain.wordbase.verbs._paraphrase import _PARAPHRASE

#calss header
class _PARAPHRASES(_PARAPHRASE, ):
	def __init__(self,): 
		_PARAPHRASE.__init__(self)
		self.name = "PARAPHRASES"
		self.specie = 'verbs'
		self.basic = "paraphrase"
		self.jsondata = {}
