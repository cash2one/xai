

#calss header
class _PRECOCIOUSLY():
	def __init__(self,): 
		self.name = "PRECOCIOUSLY"
		self.definitions = [u'in a way that is unnaturally advanced or developed']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
