

#calss header
class _SERIOUSLY():
	def __init__(self,): 
		self.name = "SERIOUSLY"
		self.definitions = [u'badly or severely: ', u'in a serious way, not joking: ', u'to consider a person, subject, or situation to be important or dangerous and worth your attention or respect: ', u'very: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
