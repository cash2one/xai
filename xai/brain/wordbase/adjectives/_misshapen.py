

#calss header
class _MISSHAPEN():
	def __init__(self,): 
		self.name = "MISSHAPEN"
		self.definitions = [u'having an unusual shape or a shape that is not natural: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
