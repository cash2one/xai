

#calss header
class _WEIRD():
	def __init__(self,): 
		self.name = "WEIRD"
		self.definitions = [u'very strange and unusual, unexpected, or not natural: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
