

#calss header
class _MEDIUM():
	def __init__(self,): 
		self.name = "MEDIUM"
		self.definitions = [u'being in the middle between an upper and lower amount, size, degree, or value: ', u'(of meat) cooked so that it is no longer red in the middle: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
