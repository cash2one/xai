

#calss header
class _CLEAR():
	def __init__(self,): 
		self.name = "CLEAR"
		self.definitions = [u'not touching, or away from: ', u'to avoid something or someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
