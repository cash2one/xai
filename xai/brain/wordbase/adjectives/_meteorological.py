

#calss header
class _METEOROLOGICAL():
	def __init__(self,): 
		self.name = "METEOROLOGICAL"
		self.definitions = [u'relating to weather conditions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
