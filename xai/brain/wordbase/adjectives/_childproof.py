

#calss header
class _CHILDPROOF():
	def __init__(self,): 
		self.name = "CHILDPROOF"
		self.definitions = [u'Childproof containers and locks cannot be opened or operated by a child: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
