

#calss header
class _COLORED():
	def __init__(self,): 
		self.name = "COLORED"
		self.definitions = [u'US spelling of  coloured ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
