

#calss header
class _REPETITIVE():
	def __init__(self,): 
		self.name = "REPETITIVE"
		self.definitions = [u'involving doing or saying the same thing several times, especially in a way that is boring: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
