

#calss header
class _ANYWHERE():
	def __init__(self,): 
		self.name = "ANYWHERE"
		self.definitions = [u'in, to, or at any place: ', u'used in questions or negatives to mean "a place": ', u'used to say that a number or amount is in a certain range but that you cannot say exactly what it is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
