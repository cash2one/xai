

#calss header
class _PROMPTLY():
	def __init__(self,): 
		self.name = "PROMPTLY"
		self.definitions = [u'quickly, without delay, or at the arranged time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
