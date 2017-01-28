

#calss header
class _FORTUNATELY():
	def __init__(self,): 
		self.name = "FORTUNATELY"
		self.definitions = [u'happening because of good luck: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
