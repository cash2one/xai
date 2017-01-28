

#calss header
class _BARRED():
	def __init__(self,): 
		self.name = "BARRED"
		self.definitions = [u'If a door is barred, a bar of wood or metal has been put across it so that it cannot be opened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
