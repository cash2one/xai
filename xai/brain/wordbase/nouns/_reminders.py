

from xai.brain.wordbase.nouns._reminder import _REMINDER

#calss header
class _REMINDERS(_REMINDER, ):
	def __init__(self,): 
		_REMINDER.__init__(self)
		self.name = "REMINDERS"
		self.specie = 'nouns'
		self.basic = "reminder"
		self.jsondata = {}
