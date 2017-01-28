

#calss header
class _CLARIFIED():
	def __init__(self,): 
		self.name = "CLARIFIED"
		self.definitions = [u'(of fat) with water and unwanted substances removed by heating: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
