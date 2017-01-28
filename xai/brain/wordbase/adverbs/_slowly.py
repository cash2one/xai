

#calss header
class _SLOWLY():
	def __init__(self,): 
		self.name = "SLOWLY"
		self.definitions = [u'at a slow speed: ', u'carefully, in order to avoid problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
