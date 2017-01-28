

#calss header
class _RACIST():
	def __init__(self,): 
		self.name = "RACIST"
		self.definitions = [u'believing that other races are not as good as your own and therefore treating them unfairly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
