

#calss header
class _KINDRED():
	def __init__(self,): 
		self.name = "KINDRED"
		self.definitions = [u'similar or related: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
