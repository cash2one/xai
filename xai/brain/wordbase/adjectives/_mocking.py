

#calss header
class _MOCKING():
	def __init__(self,): 
		self.name = "MOCKING"
		self.definitions = [u'mocking behaviour involves laughing at someone or something in an unkind way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
