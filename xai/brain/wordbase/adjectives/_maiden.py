

#calss header
class _MAIDEN():
	def __init__(self,): 
		self.name = "MAIDEN"
		self.definitions = [u'being the first of its type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
