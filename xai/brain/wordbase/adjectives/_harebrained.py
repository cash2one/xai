

#calss header
class _HAREBRAINED():
	def __init__(self,): 
		self.name = "HAREBRAINED"
		self.definitions = [u'(of plans or people) not practical or silly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
