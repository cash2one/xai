

#calss header
class _ACQUISITIVE():
	def __init__(self,): 
		self.name = "ACQUISITIVE"
		self.definitions = [u'eager to own and collect things: ', u'used to describe a company that buys other companies: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
