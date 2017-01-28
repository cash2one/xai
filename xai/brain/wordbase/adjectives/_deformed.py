

#calss header
class _DEFORMED():
	def __init__(self,): 
		self.name = "DEFORMED"
		self.definitions = [u'with a shape that has not developed normally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
