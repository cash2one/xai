

#calss header
class _FREEHAND():
	def __init__(self,): 
		self.name = "FREEHAND"
		self.definitions = [u'(of a drawing) done without the help of any special equipment for accurately creating circles, straight lines, symbols, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
