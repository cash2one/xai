

#calss header
class _YUGOSLAV():
	def __init__(self,): 
		self.name = "YUGOSLAV"
		self.definitions = [u'belonging to or relating to the former country of Yugoslavia, its people, or its language']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
