

#calss header
class _ROLLING():
	def __init__(self,): 
		self.name = "ROLLING"
		self.definitions = [u'gradual: ', u'(of hills) gently rising and falling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
