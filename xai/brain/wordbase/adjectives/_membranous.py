

#calss header
class _MEMBRANOUS():
	def __init__(self,): 
		self.name = "MEMBRANOUS"
		self.definitions = [u'relating to a membrane or like a membrane (= a very thin layer of tissue that covers or connects parts of the body): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
