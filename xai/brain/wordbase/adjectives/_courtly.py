

#calss header
class _COURTLY():
	def __init__(self,): 
		self.name = "COURTLY"
		self.definitions = [u'polite and formal in behaviour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
