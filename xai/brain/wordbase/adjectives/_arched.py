

#calss header
class _ARCHED():
	def __init__(self,): 
		self.name = "ARCHED"
		self.definitions = [u'having a shape or structure with an curve at the top, like an arch: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
