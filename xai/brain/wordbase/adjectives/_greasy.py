

#calss header
class _GREASY():
	def __init__(self,): 
		self.name = "GREASY"
		self.definitions = [u'covered with or full of fat or oil: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
