

#calss header
class _MINIMUM():
	def __init__(self,): 
		self.name = "MINIMUM"
		self.definitions = [u'at the least: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
