

#calss header
class _UNDERWEIGHT():
	def __init__(self,): 
		self.name = "UNDERWEIGHT"
		self.definitions = [u'Underweight people weigh too little and are too thin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
