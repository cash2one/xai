

#calss header
class _FEATHERY():
	def __init__(self,): 
		self.name = "FEATHERY"
		self.definitions = [u'soft or delicate, or made of many very small and delicate pieces: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
