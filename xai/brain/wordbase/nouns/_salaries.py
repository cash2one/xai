

from xai.brain.wordbase.nouns._salary import _SALARY

#calss header
class _SALARIES(_SALARY, ):
	def __init__(self,): 
		_SALARY.__init__(self)
		self.name = "SALARIES"
		self.specie = 'nouns'
		self.basic = "salary"
		self.jsondata = {}
