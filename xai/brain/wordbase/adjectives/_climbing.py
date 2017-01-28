

#calss header
class _CLIMBING():
	def __init__(self,): 
		self.name = "CLIMBING"
		self.definitions = [u'A climbing plant grows up a supporting surface: ', u'relating to the sport of climbing mountains: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
