

#calss header
class _EXTINCT():
	def __init__(self,): 
		self.name = "EXTINCT"
		self.definitions = [u'not now existing: ', u'An extinct volcano is one that is not now active (= will not explode again).']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
