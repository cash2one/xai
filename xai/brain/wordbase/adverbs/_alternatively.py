

#calss header
class _ALTERNATIVELY():
	def __init__(self,): 
		self.name = "ALTERNATIVELY"
		self.definitions = [u'used to suggest another possibility: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
