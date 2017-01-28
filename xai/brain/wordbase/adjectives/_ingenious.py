

#calss header
class _INGENIOUS():
	def __init__(self,): 
		self.name = "INGENIOUS"
		self.definitions = [u'(of a person) very intelligent and skilful, or (of a thing) skilfully made or planned and involving new ideas and methods: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
