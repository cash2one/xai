

#calss header
class _SENSUAL():
	def __init__(self,): 
		self.name = "SENSUAL"
		self.definitions = [u'expressing or suggesting physical, especially sexual, pleasure or satisfaction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
