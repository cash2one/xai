

#calss header
class _GHOULISH():
	def __init__(self,): 
		self.name = "GHOULISH"
		self.definitions = [u'ugly and unpleasant, or frightening: ', u'connected with death and unpleasant things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
