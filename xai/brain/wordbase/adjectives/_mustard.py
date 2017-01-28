

#calss header
class _MUSTARD():
	def __init__(self,): 
		self.name = "MUSTARD"
		self.definitions = [u'brownish-yellow: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
