

#calss header
class _CAFFEINATED():
	def __init__(self,): 
		self.name = "CAFFEINATED"
		self.definitions = [u'containing caffeine: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
