

#calss header
class _QUADRANGULAR():
	def __init__(self,): 
		self.name = "QUADRANGULAR"
		self.definitions = [u'having four sides: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
