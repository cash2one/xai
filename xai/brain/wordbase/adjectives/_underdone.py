

#calss header
class _UNDERDONE():
	def __init__(self,): 
		self.name = "UNDERDONE"
		self.definitions = [u'Underdone food, especially meat, is cooked for only a short time, or for less time than is necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
