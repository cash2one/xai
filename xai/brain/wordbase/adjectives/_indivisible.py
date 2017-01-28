

#calss header
class _INDIVISIBLE():
	def __init__(self,): 
		self.name = "INDIVISIBLE"
		self.definitions = [u'not able to be separated from something else or into different parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
