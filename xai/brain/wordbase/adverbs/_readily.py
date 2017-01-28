

#calss header
class _READILY():
	def __init__(self,): 
		self.name = "READILY"
		self.definitions = [u'quickly, immediately, willingly, or without any problem: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
