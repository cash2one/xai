

#calss header
class _PRINCIPLED():
	def __init__(self,): 
		self.name = "PRINCIPLED"
		self.definitions = [u'always behaving in an honest and moral way: ', u'based on moral rules: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
