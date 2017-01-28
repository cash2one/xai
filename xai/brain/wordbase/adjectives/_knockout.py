

#calss header
class _KNOCKOUT():
	def __init__(self,): 
		self.name = "KNOCKOUT"
		self.definitions = [u'extremely attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
