

#calss header
class _REPEATABLE():
	def __init__(self,): 
		self.name = "REPEATABLE"
		self.definitions = [u'something that is repeatable can be done again: ', u'too rude or offensive to be said again: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
