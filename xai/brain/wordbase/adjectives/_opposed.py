

#calss header
class _OPPOSED():
	def __init__(self,): 
		self.name = "OPPOSED"
		self.definitions = [u'completely different: ', u'rather than: ', u'to disagree with a principle or plan: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
