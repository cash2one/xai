

#calss header
class _SENSATIONALLY():
	def __init__(self,): 
		self.name = "SENSATIONALLY"
		self.definitions = [u'extremely; used to emphasize positive adjectives or adverbs: ', u'in an extremely interesting or exciting way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
