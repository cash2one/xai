

#calss header
class _GARISH():
	def __init__(self,): 
		self.name = "GARISH"
		self.definitions = [u'unpleasantly bright: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
