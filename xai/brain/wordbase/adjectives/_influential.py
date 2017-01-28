

#calss header
class _INFLUENTIAL():
	def __init__(self,): 
		self.name = "INFLUENTIAL"
		self.definitions = [u'having a lot of influence on someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
