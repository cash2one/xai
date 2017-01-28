

#calss header
class _FURIOUS():
	def __init__(self,): 
		self.name = "FURIOUS"
		self.definitions = [u'extremely angry: ', u'using a lot of effort or strength: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
