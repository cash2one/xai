

#calss header
class _CLEANLY():
	def __init__(self,): 
		self.name = "CLEANLY"
		self.definitions = [u'fairly and honestly: ', u'with smooth straight edges: ', u'equally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
