

#calss header
class _CREASED():
	def __init__(self,): 
		self.name = "CREASED"
		self.definitions = [u'with a crease or creases: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
