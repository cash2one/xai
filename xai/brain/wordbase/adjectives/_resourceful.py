

#calss header
class _RESOURCEFUL():
	def __init__(self,): 
		self.name = "RESOURCEFUL"
		self.definitions = [u'skilled at solving problems and making decisions on your own: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
