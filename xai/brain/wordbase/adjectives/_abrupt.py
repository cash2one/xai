

#calss header
class _ABRUPT():
	def __init__(self,): 
		self.name = "ABRUPT"
		self.definitions = [u'sudden and unexpected, and often unpleasant: ', u'using too few words when talking, in a way that seems rude and unfriendly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
