

#calss header
class _TOWERING():
	def __init__(self,): 
		self.name = "TOWERING"
		self.definitions = [u'very high and making people feel respect: ', u'very great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
