

#calss header
class _DIAGONAL():
	def __init__(self,): 
		self.name = "DIAGONAL"
		self.definitions = [u'A diagonal line is straight and sloping, not horizontal or vertical, for example joining two opposite corners of a square or other flat shape with four sides: ', u'moving in a diagonal line: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
