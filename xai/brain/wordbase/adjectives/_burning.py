

#calss header
class _BURNING():
	def __init__(self,): 
		self.name = "BURNING"
		self.definitions = [u'producing flames: ', u'very hot: ', u'A burning desire, need, etc., is one that is very strong: ', u'a subject or question that must be dealt with or answered quickly']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
