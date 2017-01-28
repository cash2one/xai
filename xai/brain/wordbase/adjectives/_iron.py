

#calss header
class _IRON():
	def __init__(self,): 
		self.name = "IRON"
		self.definitions = [u'very strong physically, mentally, or emotionally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
