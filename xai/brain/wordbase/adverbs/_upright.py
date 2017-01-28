

#calss header
class _UPRIGHT():
	def __init__(self,): 
		self.name = "UPRIGHT"
		self.definitions = [u'vertical and as straight as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
