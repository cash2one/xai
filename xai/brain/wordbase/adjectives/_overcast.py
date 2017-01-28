

#calss header
class _OVERCAST():
	def __init__(self,): 
		self.name = "OVERCAST"
		self.definitions = [u'with clouds in the sky and therefore not bright and sunny: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
