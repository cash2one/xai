

#calss header
class _SCORELESS():
	def __init__(self,): 
		self.name = "SCORELESS"
		self.definitions = [u'In a scoreless game, no goals or points are scored: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
