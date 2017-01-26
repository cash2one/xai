

from xai.brain.wordbase.verbs._paraphrase import _PARAPHRASE

#calss header
class _PARAPHRASING(_PARAPHRASE, ):
	def __init__(self,): 
		_PARAPHRASE.__init__(self)
		self.name = "PARAPHRASING"
		self.specie = 'verbs'
		self.basic = "paraphrase"
		self.jsondata = {}
