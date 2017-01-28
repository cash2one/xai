

#calss header
class _UPSTATE():
	def __init__(self,): 
		self.name = "UPSTATE"
		self.definitions = [u'towards or of the northern parts of a state in the US, especially those that are far from cities where a lot of people live: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
