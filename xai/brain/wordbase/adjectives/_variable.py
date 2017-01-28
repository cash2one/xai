

#calss header
class _VARIABLE():
	def __init__(self,): 
		self.name = "VARIABLE"
		self.definitions = [u'likely to change often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
