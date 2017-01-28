

#calss header
class _DRACONIAN():
	def __init__(self,): 
		self.name = "DRACONIAN"
		self.definitions = [u'Draconian laws, government actions, etc. are extremely severe, or go further than what is right or necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
