

#calss header
class _INFLEXIBLE():
	def __init__(self,): 
		self.name = "INFLEXIBLE"
		self.definitions = [u'(especially of opinions and rules) fixed and unable or unwilling to change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
