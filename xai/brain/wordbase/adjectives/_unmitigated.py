

#calss header
class _UNMITIGATED():
	def __init__(self,): 
		self.name = "UNMITIGATED"
		self.definitions = [u'complete, often describing something bad or unsuccessful that has no good or positive points: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
