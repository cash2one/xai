

#calss header
class _BUT():
	def __init__(self,): 
		self.name = "BUT"
		self.definitions = [u'used to give force to a statement: ', u'only; just: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
