

#calss header
class _RIGIDLY():
	def __init__(self,): 
		self.name = "RIGIDLY"
		self.definitions = [u'in a stiff or fixed way, without bending or moving: ', u'not willing or able to change according to circumstances: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
