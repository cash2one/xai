

#calss header
class _KNOTTY():
	def __init__(self,): 
		self.name = "KNOTTY"
		self.definitions = [u'(of a problem or difficulty) complicated and difficult to solve: ', u'with a lot of knots: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
