

#calss header
class _SLIPPERY():
	def __init__(self,): 
		self.name = "SLIPPERY"
		self.definitions = [u'If something is slippery, it is wet or smooth so that it slides easily or causes something to slide: ', u'Someone who is slippery cannot be trusted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
