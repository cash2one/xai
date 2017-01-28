

#calss header
class _NOWHERE():
	def __init__(self,): 
		self.name = "NOWHERE"
		self.definitions = [u'in, at, or to no place; not anywhere: ', u'not in a successful or winning position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
