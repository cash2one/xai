

#calss header
class _STODGY():
	def __init__(self,): 
		self.name = "STODGY"
		self.definitions = [u'Stodgy food is heavy and unhealthy, sometimes in an unpleasant way: ', u'boring, serious, and formal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
