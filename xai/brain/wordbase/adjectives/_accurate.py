

#calss header
class _ACCURATE():
	def __init__(self,): 
		self.name = "ACCURATE"
		self.definitions = [u'correct, exact, and without any mistakes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
