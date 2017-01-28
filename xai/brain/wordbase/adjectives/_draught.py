

#calss header
class _DRAUGHT():
	def __init__(self,): 
		self.name = "DRAUGHT"
		self.definitions = [u'(of drinks such as beer) stored in and served from large containers, especially barrels: ', u'(of animals) used for pulling heavy loads, vehicles, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
