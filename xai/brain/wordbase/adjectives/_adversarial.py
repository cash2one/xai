

#calss header
class _ADVERSARIAL():
	def __init__(self,): 
		self.name = "ADVERSARIAL"
		self.definitions = [u'involving people opposing or disagreeing with each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
