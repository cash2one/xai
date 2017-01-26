

from xai.brain.wordbase.verbs._mail import _MAIL

#calss header
class _MAILING(_MAIL, ):
	def __init__(self,): 
		_MAIL.__init__(self)
		self.name = "MAILING"
		self.specie = 'verbs'
		self.basic = "mail"
		self.jsondata = {}
