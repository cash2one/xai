

#calss header
class _OVERMUCH():
	def __init__(self,): 
		self.name = "OVERMUCH"
		self.definitions = [u'(especially in negatives) too much or very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
