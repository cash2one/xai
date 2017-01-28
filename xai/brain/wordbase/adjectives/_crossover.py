

#calss header
class _CROSSOVER():
	def __init__(self,): 
		self.name = "CROSSOVER"
		self.definitions = [u'used to refer to a musician who has changed to a different style of music, or to their music: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
