

#calss header
class _BOILED():
	def __init__(self,): 
		self.name = "BOILED"
		self.definitions = [u'(of food) cooked in water that is boiling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
