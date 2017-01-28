

#calss header
class _VEGETABLE():
	def __init__(self,): 
		self.name = "VEGETABLE"
		self.definitions = [u'made or obtained from a plant, or growing in the form of a plant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
