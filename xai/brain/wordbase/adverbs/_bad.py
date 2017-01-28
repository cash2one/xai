

#calss header
class _BAD():
	def __init__(self,): 
		self.name = "BAD"
		self.definitions = [u'informal for badly (= very much): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
