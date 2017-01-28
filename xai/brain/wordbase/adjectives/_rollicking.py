

#calss header
class _ROLLICKING():
	def __init__(self,): 
		self.name = "ROLLICKING"
		self.definitions = [u'happy, energetic, and often noisy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
