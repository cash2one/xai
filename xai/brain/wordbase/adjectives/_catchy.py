

#calss header
class _CATCHY():
	def __init__(self,): 
		self.name = "CATCHY"
		self.definitions = [u'(especially of a tune or song) pleasing and easy to remember: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
