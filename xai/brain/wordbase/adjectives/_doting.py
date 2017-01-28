

#calss header
class _DOTING():
	def __init__(self,): 
		self.name = "DOTING"
		self.definitions = [u'showing that you love someone very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
