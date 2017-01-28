

#calss header
class _COMPLETELY():
	def __init__(self,): 
		self.name = "COMPLETELY"
		self.definitions = [u'in every way or as much as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
