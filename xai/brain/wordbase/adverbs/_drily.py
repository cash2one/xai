

#calss header
class _DRILY():
	def __init__(self,): 
		self.name = "DRILY"
		self.definitions = [u'being funny in a way that is not obvious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
