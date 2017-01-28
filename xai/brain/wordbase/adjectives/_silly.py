

#calss header
class _SILLY():
	def __init__(self,): 
		self.name = "SILLY"
		self.definitions = [u'showing little thought or judgment: ', u'embarrassed; afraid that people will laugh at you: ', u'not important, serious, or practical: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
