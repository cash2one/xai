

#calss header
class _SILKY():
	def __init__(self,): 
		self.name = "SILKY"
		self.definitions = [u'soft and smooth, like silk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
