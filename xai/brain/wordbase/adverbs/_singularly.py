

#calss header
class _SINGULARLY():
	def __init__(self,): 
		self.name = "SINGULARLY"
		self.definitions = [u'to an unusual degree: ', u'strangely']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
