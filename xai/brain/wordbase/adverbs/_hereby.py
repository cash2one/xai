

#calss header
class _HEREBY():
	def __init__(self,): 
		self.name = "HEREBY"
		self.definitions = [u'with these words or with this action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
