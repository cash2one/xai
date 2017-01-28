

#calss header
class _INNERMOST():
	def __init__(self,): 
		self.name = "INNERMOST"
		self.definitions = [u'most secret and hidden: ', u'nearest to the centre: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
