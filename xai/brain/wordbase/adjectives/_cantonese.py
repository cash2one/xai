

#calss header
class _CANTONESE():
	def __init__(self,): 
		self.name = "CANTONESE"
		self.definitions = [u'belonging or relating to the Guandong region in the south of China, its people, or its language: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
