

#calss header
class _SMALL():
	def __init__(self,): 
		self.name = "SMALL"
		self.definitions = [u'in a small size: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
