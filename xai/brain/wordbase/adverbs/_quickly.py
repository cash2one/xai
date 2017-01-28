

#calss header
class _QUICKLY():
	def __init__(self,): 
		self.name = "QUICKLY"
		self.definitions = [u'at a fast speed: ', u'after only a very short time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
