

#calss header
class _SATED():
	def __init__(self,): 
		self.name = "SATED"
		self.definitions = [u'having had more of something than you can easily have at one time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
