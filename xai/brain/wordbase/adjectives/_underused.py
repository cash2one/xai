

#calss header
class _UNDERUSED():
	def __init__(self,): 
		self.name = "UNDERUSED"
		self.definitions = [u'not used as much as it could or should be: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
