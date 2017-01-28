

#calss header
class _BUST():
	def __init__(self,): 
		self.name = "BUST"
		self.definitions = [u'broken: ', u'If a company goes bust, it is forced to close because it is financially unsuccessful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
