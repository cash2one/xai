

#calss header
class _MINCED():
	def __init__(self,): 
		self.name = "MINCED"
		self.definitions = [u'(especially of meat) having been cut up into very small pieces: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
