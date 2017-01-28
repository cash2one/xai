

#calss header
class _SWELTERING():
	def __init__(self,): 
		self.name = "SWELTERING"
		self.definitions = [u'extremely and uncomfortably hot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
