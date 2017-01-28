

#calss header
class _READY():
	def __init__(self,): 
		self.name = "READY"
		self.definitions = [u'prepared and suitable for fast activity: ', u'waiting and prepared to act: ', u'quick with answers, jokes, solutions, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
