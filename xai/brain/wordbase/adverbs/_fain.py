

#calss header
class _FAIN():
	def __init__(self,): 
		self.name = "FAIN"
		self.definitions = [u'willingly or happily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
