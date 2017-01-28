

#calss header
class _PERCEPTIBLE():
	def __init__(self,): 
		self.name = "PERCEPTIBLE"
		self.definitions = [u'that can be seen, heard, or noticed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
