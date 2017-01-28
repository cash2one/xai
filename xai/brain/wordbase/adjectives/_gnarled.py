

#calss header
class _GNARLED():
	def __init__(self,): 
		self.name = "GNARLED"
		self.definitions = [u'rough and twisted, especially because of old age or no protection from bad weather: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
