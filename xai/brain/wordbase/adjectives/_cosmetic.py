

#calss header
class _COSMETIC():
	def __init__(self,): 
		self.name = "COSMETIC"
		self.definitions = [u'Corrective changes, etc. are intended to make you believe that something is better when, really, the problem has not been solved: ', u'used to refer to substances or treatments that are intended to improve your appearance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
