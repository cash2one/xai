

#calss header
class _UNDEFINED():
	def __init__(self,): 
		self.name = "UNDEFINED"
		self.definitions = [u'not clearly described, stated, or known: ', u'not having been given a definition (= a statement explaining the meaning of something): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
