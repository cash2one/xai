

#calss header
class _CONSTANTLY():
	def __init__(self,): 
		self.name = "CONSTANTLY"
		self.definitions = [u'all the time or often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
