

#calss header
class _VITREOUS():
	def __init__(self,): 
		self.name = "VITREOUS"
		self.definitions = [u'made of or similar to glass: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
