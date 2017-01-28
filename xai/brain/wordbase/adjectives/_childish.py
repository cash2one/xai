

#calss header
class _CHILDISH():
	def __init__(self,): 
		self.name = "CHILDISH"
		self.definitions = [u'typical of a child: ', u'If an adult is childish, they behave badly in a way that would be expected of a child: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
