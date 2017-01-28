

#calss header
class _SUPERCHARGED():
	def __init__(self,): 
		self.name = "SUPERCHARGED"
		self.definitions = [u'very fast or energetic: ', u'containing or expressing very strong emotions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
