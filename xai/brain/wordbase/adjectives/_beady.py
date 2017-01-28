

#calss header
class _BEADY():
	def __init__(self,): 
		self.name = "BEADY"
		self.definitions = [u"(of eyes) small and bright, especially like a bird's eyes: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
