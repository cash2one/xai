

#calss header
class _ASEPTIC():
	def __init__(self,): 
		self.name = "ASEPTIC"
		self.definitions = [u'medically clean or without infection: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
