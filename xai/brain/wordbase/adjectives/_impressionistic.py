

#calss header
class _IMPRESSIONISTIC():
	def __init__(self,): 
		self.name = "IMPRESSIONISTIC"
		self.definitions = [u'giving a general view or idea of something instead of particular details or facts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
