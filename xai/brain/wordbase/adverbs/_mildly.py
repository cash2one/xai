

#calss header
class _MILDLY():
	def __init__(self,): 
		self.name = "MILDLY"
		self.definitions = [u'slightly: ', u'in a gentle way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
