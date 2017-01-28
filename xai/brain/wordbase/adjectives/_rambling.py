

#calss header
class _RAMBLING():
	def __init__(self,): 
		self.name = "RAMBLING"
		self.definitions = [u'too long and confused: ', u'large and spreading out in many different directions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
