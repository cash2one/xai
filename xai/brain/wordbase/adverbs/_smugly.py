

#calss header
class _SMUGLY():
	def __init__(self,): 
		self.name = "SMUGLY"
		self.definitions = [u'in a way that shows too much satisfaction or confidence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
