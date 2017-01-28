

#calss header
class _DOUBLE():
	def __init__(self,): 
		self.name = "DOUBLE"
		self.definitions = [u'twice the size, amount, price, etc., or consisting of two similar things together: ', u'A double flower or plant is a flower with more than the usual number of petals: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
