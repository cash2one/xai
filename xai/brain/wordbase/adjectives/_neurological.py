

#calss header
class _NEUROLOGICAL():
	def __init__(self,): 
		self.name = "NEUROLOGICAL"
		self.definitions = [u'relating to nerves: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
