

#calss header
class _ORNERY():
	def __init__(self,): 
		self.name = "ORNERY"
		self.definitions = [u'likely to get angry and argue with people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
