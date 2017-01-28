

#calss header
class _CONTRAPUNTAL():
	def __init__(self,): 
		self.name = "CONTRAPUNTAL"
		self.definitions = [u'Contrapuntal music has two or more separate tunes that are played or sung at the same time.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
