

#calss header
class _TIRELESS():
	def __init__(self,): 
		self.name = "TIRELESS"
		self.definitions = [u'working energetically and continuously: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
