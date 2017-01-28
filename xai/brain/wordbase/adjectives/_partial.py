

#calss header
class _PARTIAL():
	def __init__(self,): 
		self.name = "PARTIAL"
		self.definitions = [u'not complete: ', u'influenced by the fact that you personally prefer or approve of something, so that you do not judge fairly: ', u'having a liking for something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
