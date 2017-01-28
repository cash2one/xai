

#calss header
class _POLYUNSATURATED():
	def __init__(self,): 
		self.name = "POLYUNSATURATED"
		self.definitions = [u'Polyunsaturated fat or oil has a chemical structure that does not easily change into cholesterol (= a substance containing a lot of fat that can cause heart disease) because it contains several double bonds: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
