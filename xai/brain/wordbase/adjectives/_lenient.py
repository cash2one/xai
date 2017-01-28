

#calss header
class _LENIENT():
	def __init__(self,): 
		self.name = "LENIENT"
		self.definitions = [u'not as severe or strong in punishment or judgment as would be expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
