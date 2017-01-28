

#calss header
class _MACROBIOTIC():
	def __init__(self,): 
		self.name = "MACROBIOTIC"
		self.definitions = [u'Macrobiotic food is arranged into groups according to special principles, grown without chemicals, and thought to be very healthy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
