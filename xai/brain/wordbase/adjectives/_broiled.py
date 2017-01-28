

#calss header
class _BROILED():
	def __init__(self,): 
		self.name = "BROILED"
		self.definitions = [u'(of food) cooked under a very hot surface in a cooker: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
