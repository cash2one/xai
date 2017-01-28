

#calss header
class _HEARTILY():
	def __init__(self,): 
		self.name = "HEARTILY"
		self.definitions = [u'enthusiastically, energetically, and often loudly: ', u'completely or very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
