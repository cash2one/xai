

#calss header
class _STUPENDOUS():
	def __init__(self,): 
		self.name = "STUPENDOUS"
		self.definitions = [u'very surprising, usually in a pleasing way, especially by being large in amount or size: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
