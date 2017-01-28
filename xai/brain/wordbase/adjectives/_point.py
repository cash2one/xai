

#calss header
class _POINT():
	def __init__(self,): 
		self.name = "POINT"
		self.definitions = [u'relating to when a ballet dancer dances on their toes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
