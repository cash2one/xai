

#calss header
class _COASTAL():
	def __init__(self,): 
		self.name = "COASTAL"
		self.definitions = [u'positioned on, or relating to the coast: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
