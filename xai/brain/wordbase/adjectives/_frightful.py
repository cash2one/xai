

#calss header
class _FRIGHTFUL():
	def __init__(self,): 
		self.name = "FRIGHTFUL"
		self.definitions = [u'used to emphasize what you are saying, especially how bad something is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
