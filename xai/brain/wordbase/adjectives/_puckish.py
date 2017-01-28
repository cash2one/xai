

#calss header
class _PUCKISH():
	def __init__(self,): 
		self.name = "PUCKISH"
		self.definitions = [u'liking to make jokes about other people and play silly tricks on them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
