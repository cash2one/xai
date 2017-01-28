

#calss header
class _UNSTEADY():
	def __init__(self,): 
		self.name = "UNSTEADY"
		self.definitions = [u'moving slightly from side to side, as if you might fall: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
