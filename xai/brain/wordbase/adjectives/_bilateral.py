

#calss header
class _BILATERAL():
	def __init__(self,): 
		self.name = "BILATERAL"
		self.definitions = [u'involving two groups or countries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
