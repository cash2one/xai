

#calss header
class _ACCUSTOMED():
	def __init__(self,): 
		self.name = "ACCUSTOMED"
		self.definitions = [u'familiar with something: ', u'usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
