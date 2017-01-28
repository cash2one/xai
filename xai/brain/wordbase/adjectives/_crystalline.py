

#calss header
class _CRYSTALLINE():
	def __init__(self,): 
		self.name = "CRYSTALLINE"
		self.definitions = [u'clear and bright like crystal: ', u'A crystalline substance has become solid, with regular shapes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
