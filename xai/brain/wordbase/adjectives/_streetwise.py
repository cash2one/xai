

#calss header
class _STREETWISE():
	def __init__(self,): 
		self.name = "STREETWISE"
		self.definitions = [u'able to deal successfully with dangerous or difficult situations in big towns or cities where there is a lot of crime: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
