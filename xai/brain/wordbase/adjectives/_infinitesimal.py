

#calss header
class _INFINITESIMAL():
	def __init__(self,): 
		self.name = "INFINITESIMAL"
		self.definitions = [u'extremely small: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
