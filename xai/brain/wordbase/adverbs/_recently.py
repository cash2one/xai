

#calss header
class _RECENTLY():
	def __init__(self,): 
		self.name = "RECENTLY"
		self.definitions = [u'not long ago, or at a time that started not long ago: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
