

#calss header
class _UNQUESTIONED():
	def __init__(self,): 
		self.name = "UNQUESTIONED"
		self.definitions = [u'accepted as true or right by everyone, or trusted and respected by everyone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
