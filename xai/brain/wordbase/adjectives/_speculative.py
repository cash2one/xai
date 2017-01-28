

#calss header
class _SPECULATIVE():
	def __init__(self,): 
		self.name = "SPECULATIVE"
		self.definitions = [u'based on a guess and not on information: ', u'bought or done in order to make a profit in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
