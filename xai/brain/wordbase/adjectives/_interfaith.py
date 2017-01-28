

#calss header
class _INTERFAITH():
	def __init__(self,): 
		self.name = "INTERFAITH"
		self.definitions = [u'relating to activities involving members of different religions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
