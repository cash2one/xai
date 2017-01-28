

#calss header
class _AWHILE():
	def __init__(self,): 
		self.name = "AWHILE"
		self.definitions = [u'for a short time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
