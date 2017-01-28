

#calss header
class _MORONIC():
	def __init__(self,): 
		self.name = "MORONIC"
		self.definitions = [u'very stupid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
