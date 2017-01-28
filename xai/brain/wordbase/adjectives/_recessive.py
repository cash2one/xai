

#calss header
class _RECESSIVE():
	def __init__(self,): 
		self.name = "RECESSIVE"
		self.definitions = [u'(of genes and the physical qualities they control) only appearing in a child if both parents supply the controlling gene']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
