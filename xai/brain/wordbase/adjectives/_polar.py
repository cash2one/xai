

#calss header
class _POLAR():
	def __init__(self,): 
		self.name = "POLAR"
		self.definitions = [u'relating to the North or South Pole or the areas around them: ', u'Polar opposites are complete opposites: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
