

#calss header
class _WANTON():
	def __init__(self,): 
		self.name = "WANTON"
		self.definitions = [u'(of something bad, such as damage, cruelty, waste) extreme and showing no care at all: ', u'(of a woman) behaving or appearing in a very sexual way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
