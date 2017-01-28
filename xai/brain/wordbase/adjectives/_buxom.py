

#calss header
class _BUXOM():
	def __init__(self,): 
		self.name = "BUXOM"
		self.definitions = [u'(of a woman) healthy-looking and slightly fat, with large breasts']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
