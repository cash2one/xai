

#calss header
class _THEREOF():
	def __init__(self,): 
		self.name = "THEREOF"
		self.definitions = [u'of or about the thing just mentioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
