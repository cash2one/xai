

#calss header
class _TERRIBLE():
	def __init__(self,): 
		self.name = "TERRIBLE"
		self.definitions = [u'very unpleasant or serious or of low quality: ', u'very bad at doing something: ', u'used to emphasize the great degree of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
