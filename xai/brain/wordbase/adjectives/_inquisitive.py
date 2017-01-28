

#calss header
class _INQUISITIVE():
	def __init__(self,): 
		self.name = "INQUISITIVE"
		self.definitions = [u'wanting to discover as much as you can about things, sometimes in a way that annoys people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
