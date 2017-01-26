

from xai.brain.wordbase.verbs._mail import _MAIL

#calss header
class _MAILED(_MAIL, ):
	def __init__(self,): 
		_MAIL.__init__(self)
		self.name = "MAILED"
		self.specie = 'verbs'
		self.basic = "mail"
		self.jsondata = {}
