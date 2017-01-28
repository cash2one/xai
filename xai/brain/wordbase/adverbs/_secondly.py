

#calss header
class _SECONDLY():
	def __init__(self,): 
		self.name = "SECONDLY"
		self.definitions = [u'used when stating the second of two or more reasons or pieces of information: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
