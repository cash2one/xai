

#calss header
class _OBSERVANT():
	def __init__(self,): 
		self.name = "OBSERVANT"
		self.definitions = [u'good or quick at noticing things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
