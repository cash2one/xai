

#calss header
class _UNATTRACTIVE():
	def __init__(self,): 
		self.name = "UNATTRACTIVE"
		self.definitions = [u'unpleasant to look at: ', u'lacking good or positive features: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
