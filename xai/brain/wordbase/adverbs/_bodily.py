

#calss header
class _BODILY():
	def __init__(self,): 
		self.name = "BODILY"
		self.definitions = [u'If you lift or carry someone bodily, you lift or carry them in your arms: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
