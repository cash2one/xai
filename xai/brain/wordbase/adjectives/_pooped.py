

#calss header
class _POOPED():
	def __init__(self,): 
		self.name = "POOPED"
		self.definitions = [u'breathing with difficulty because you have been doing physical exercise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
