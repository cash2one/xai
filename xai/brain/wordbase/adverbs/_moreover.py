

#calss header
class _MOREOVER():
	def __init__(self,): 
		self.name = "MOREOVER"
		self.definitions = [u'(used to add information) also and more importantly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
