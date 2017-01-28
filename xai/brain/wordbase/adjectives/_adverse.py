

#calss header
class _ADVERSE():
	def __init__(self,): 
		self.name = "ADVERSE"
		self.definitions = [u'having a negative or harmful effect on something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
