

#calss header
class _EMINENT():
	def __init__(self,): 
		self.name = "EMINENT"
		self.definitions = [u'famous, respected, or important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
