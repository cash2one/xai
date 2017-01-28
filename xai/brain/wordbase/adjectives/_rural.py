

#calss header
class _RURAL():
	def __init__(self,): 
		self.name = "RURAL"
		self.definitions = [u'in, of, or like the countryside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
