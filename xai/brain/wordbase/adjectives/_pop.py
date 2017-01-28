

#calss header
class _POP():
	def __init__(self,): 
		self.name = "POP"
		self.definitions = [u'enjoyed by many people and easy to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
