

#calss header
class _GIRLISH():
	def __init__(self,): 
		self.name = "GIRLISH"
		self.definitions = [u'Girlish behaviour or characteristics are typical of a girl: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
