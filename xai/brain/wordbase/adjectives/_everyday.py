

#calss header
class _EVERYDAY():
	def __init__(self,): 
		self.name = "EVERYDAY"
		self.definitions = [u'ordinary, typical, or usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
