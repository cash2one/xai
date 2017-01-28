

#calss header
class _CLOSED():
	def __init__(self,): 
		self.name = "CLOSED"
		self.definitions = [u'not open: ', u'not open for business: ', u'finished and therefore not able to be discussed any more : ', u'not wanting to accept new ideas, people, customs, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
