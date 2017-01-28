

#calss header
class _ANODYNE():
	def __init__(self,): 
		self.name = "ANODYNE"
		self.definitions = [u'intended to avoid causing offence or disagreement, especially by not expressing strong feelings or opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
