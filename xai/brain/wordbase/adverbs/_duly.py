

#calss header
class _DULY():
	def __init__(self,): 
		self.name = "DULY"
		self.definitions = [u'in the correct way or at the correct time; as expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
