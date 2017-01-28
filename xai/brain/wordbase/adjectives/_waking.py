

#calss header
class _WAKING():
	def __init__(self,): 
		self.name = "WAKING"
		self.definitions = [u'used to refer to a period of time or an experience during which you are awake: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
