

#calss header
class _INJUDICIOUS():
	def __init__(self,): 
		self.name = "INJUDICIOUS"
		self.definitions = [u'showing bad judgment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
