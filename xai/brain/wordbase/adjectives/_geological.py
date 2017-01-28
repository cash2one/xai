

#calss header
class _GEOLOGICAL():
	def __init__(self,): 
		self.name = "GEOLOGICAL"
		self.definitions = [u'relating to geology, or to the geology of a particular area or place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
