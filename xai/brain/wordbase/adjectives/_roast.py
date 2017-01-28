

#calss header
class _ROAST():
	def __init__(self,): 
		self.name = "ROAST"
		self.definitions = [u'Roast meat or vegetables have been cooked in an oven or over a fire: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
