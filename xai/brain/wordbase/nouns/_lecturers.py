

from xai.brain.wordbase.nouns._lecturer import _LECTURER

#calss header
class _LECTURERS(_LECTURER, ):
	def __init__(self,): 
		_LECTURER.__init__(self)
		self.name = "LECTURERS"
		self.specie = 'nouns'
		self.basic = "lecturer"
		self.jsondata = {}
