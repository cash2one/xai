

#calss header
class _PRONTO():
	def __init__(self,): 
		self.name = "PRONTO"
		self.definitions = [u'quickly and without delay: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
