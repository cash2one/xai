

#calss header
class _MOLAR():
	def __init__(self,): 
		self.name = "MOLAR"
		self.definitions = [u'containing one mole of a substance in each litre of a liquid']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
