

#calss header
class _SOMEWAY():
	def __init__(self,): 
		self.name = "SOMEWAY"
		self.definitions = [u'informal for  somehow : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
