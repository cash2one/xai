

#calss header
class _TORRID():
	def __init__(self,): 
		self.name = "TORRID"
		self.definitions = [u'involving strong emotions, especially those of sexual love: ', u'extremely hot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
