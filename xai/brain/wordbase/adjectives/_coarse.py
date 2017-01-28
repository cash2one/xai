

#calss header
class _COARSE():
	def __init__(self,): 
		self.name = "COARSE"
		self.definitions = [u'rough and not smooth or soft, or not in very small pieces: ', u'rude and offensive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
