

#calss header
class _EVIDENTLY():
	def __init__(self,): 
		self.name = "EVIDENTLY"
		self.definitions = [u'in a way that is easy to see: ', u'used to say what people believe is true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
