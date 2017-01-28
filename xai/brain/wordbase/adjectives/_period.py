

#calss header
class _PERIOD():
	def __init__(self,): 
		self.name = "PERIOD"
		self.definitions = [u'the clothes or furniture of a particular time in history: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
