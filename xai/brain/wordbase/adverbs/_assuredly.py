

#calss header
class _ASSUREDLY():
	def __init__(self,): 
		self.name = "ASSUREDLY"
		self.definitions = [u'confidently: ', u'certainly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
