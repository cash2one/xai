

#calss header
class _NOTABLY():
	def __init__(self,): 
		self.name = "NOTABLY"
		self.definitions = [u'especially or most importantly: ', u'to an important degree, or in a way that can or should be noticed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
