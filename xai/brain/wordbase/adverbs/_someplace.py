

#calss header
class _SOMEPLACE():
	def __init__(self,): 
		self.name = "SOMEPLACE"
		self.definitions = [u'somewhere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
