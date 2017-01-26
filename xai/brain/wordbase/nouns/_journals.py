

from xai.brain.wordbase.nouns._journal import _JOURNAL

#calss header
class _JOURNALS(_JOURNAL, ):
	def __init__(self,): 
		_JOURNAL.__init__(self)
		self.name = "JOURNALS"
		self.specie = 'nouns'
		self.basic = "journal"
		self.jsondata = {}
