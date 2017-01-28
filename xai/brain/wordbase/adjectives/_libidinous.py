

#calss header
class _LIBIDINOUS():
	def __init__(self,): 
		self.name = "LIBIDINOUS"
		self.definitions = [u'having or showing strong sexual desires']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
