

#calss header
class _RAUNCHY():
	def __init__(self,): 
		self.name = "RAUNCHY"
		self.definitions = [u'connected with sex in a very clear and obvious way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
