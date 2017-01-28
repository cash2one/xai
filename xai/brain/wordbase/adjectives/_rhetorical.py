

#calss header
class _RHETORICAL():
	def __init__(self,): 
		self.name = "RHETORICAL"
		self.definitions = [u'Rhetorical speech or writing is intended to seem important or influence people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
