

#calss header
class _SILKEN():
	def __init__(self,): 
		self.name = "SILKEN"
		self.definitions = [u'soft, smooth, and shiny like silk: ', u'a silken sound is one that is pleasant because it is very smooth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
