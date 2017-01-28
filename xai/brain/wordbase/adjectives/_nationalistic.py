

#calss header
class _NATIONALISTIC():
	def __init__(self,): 
		self.name = "NATIONALISTIC"
		self.definitions = [u'being too proud of your own country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
