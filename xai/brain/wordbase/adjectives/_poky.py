

#calss header
class _POKY():
	def __init__(self,): 
		self.name = "POKY"
		self.definitions = [u'A poky room, house, or other place is unpleasantly small and uncomfortable: ', u'slow: ', u'(of a car) fast: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
