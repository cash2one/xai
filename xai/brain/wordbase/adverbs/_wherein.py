

#calss header
class _WHEREIN():
	def __init__(self,): 
		self.name = "WHEREIN"
		self.definitions = [u'in which, or in which part: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
