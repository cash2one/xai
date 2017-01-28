

#calss header
class _PRETERNATURAL():
	def __init__(self,): 
		self.name = "PRETERNATURAL"
		self.definitions = [u'more than is usual or natural: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
