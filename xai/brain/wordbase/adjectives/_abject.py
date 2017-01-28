

#calss header
class _ABJECT():
	def __init__(self,): 
		self.name = "ABJECT"
		self.definitions = [u'the state of being extremely unhappy, poor, unsuccessful, etc.: ', u'showing no pride or respect for yourself: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
