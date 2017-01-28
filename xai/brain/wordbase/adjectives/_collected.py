

#calss header
class _COLLECTED():
	def __init__(self,): 
		self.name = "COLLECTED"
		self.definitions = [u'brought together in one book or series of books: ', u'showing control over your feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
