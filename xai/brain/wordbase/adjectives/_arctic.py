

#calss header
class _ARCTIC():
	def __init__(self,): 
		self.name = "ARCTIC"
		self.definitions = [u'belonging or relating to the Arctic: ', u'very cold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
