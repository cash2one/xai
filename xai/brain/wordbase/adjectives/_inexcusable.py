

#calss header
class _INEXCUSABLE():
	def __init__(self,): 
		self.name = "INEXCUSABLE"
		self.definitions = [u'(of behaviour) too bad to be accepted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
