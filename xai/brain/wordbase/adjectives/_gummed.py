

#calss header
class _GUMMED():
	def __init__(self,): 
		self.name = "GUMMED"
		self.definitions = [u'sticky or with glue on the surface: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
