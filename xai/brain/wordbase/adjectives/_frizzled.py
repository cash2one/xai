

#calss header
class _FRIZZLED():
	def __init__(self,): 
		self.name = "FRIZZLED"
		self.definitions = [u'(of food) fried for too long, making it burnt and unpleasant to eat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
