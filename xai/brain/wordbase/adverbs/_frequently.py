

#calss header
class _FREQUENTLY():
	def __init__(self,): 
		self.name = "FREQUENTLY"
		self.definitions = [u'often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
