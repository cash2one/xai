

#calss header
class _PROPER():
	def __init__(self,): 
		self.name = "PROPER"
		self.definitions = [u'real, satisfactory, suitable, or correct: ', u'showing standards of behaviour that are socially and morally acceptable: ', u'belonging to the main, most important, or typical part: ', u'complete: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
