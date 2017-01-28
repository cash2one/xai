

#calss header
class _NOWADAYS():
	def __init__(self,): 
		self.name = "NOWADAYS"
		self.definitions = [u'at the present time, in comparison to the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
