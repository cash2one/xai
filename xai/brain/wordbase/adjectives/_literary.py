

#calss header
class _LITERARY():
	def __init__(self,): 
		self.name = "LITERARY"
		self.definitions = [u'connected with literature: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
