

from xai.brain.wordbase.nouns._loanword import _LOANWORD

#calss header
class _LOANWORDS(_LOANWORD, ):
	def __init__(self,): 
		_LOANWORD.__init__(self)
		self.name = "LOANWORDS"
		self.specie = 'nouns'
		self.basic = "loanword"
		self.jsondata = {}
