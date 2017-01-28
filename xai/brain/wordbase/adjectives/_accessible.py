

#calss header
class _ACCESSIBLE():
	def __init__(self,): 
		self.name = "ACCESSIBLE"
		self.definitions = [u'able to be reached or easily got: ', u'easy to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
