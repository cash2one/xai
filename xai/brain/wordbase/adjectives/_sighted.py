

#calss header
class _SIGHTED():
	def __init__(self,): 
		self.name = "SIGHTED"
		self.definitions = [u'able to see']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
