

#calss header
class _LEGIT():
	def __init__(self,): 
		self.name = "LEGIT"
		self.definitions = [u'used to mean "actually" when you want to say that you think something is very surprising or difficult to believe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
