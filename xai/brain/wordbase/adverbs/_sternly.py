

#calss header
class _STERNLY():
	def __init__(self,): 
		self.name = "STERNLY"
		self.definitions = [u'in a way that shows disapproval: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
