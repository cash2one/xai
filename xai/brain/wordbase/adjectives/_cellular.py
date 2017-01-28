

#calss header
class _CELLULAR():
	def __init__(self,): 
		self.name = "CELLULAR"
		self.definitions = [u'connected with the cells of a plant or animal', u'made of small parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
