

#calss header
class _PHOTOSENSITIVE():
	def __init__(self,): 
		self.name = "PHOTOSENSITIVE"
		self.definitions = [u'reacting to light: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
