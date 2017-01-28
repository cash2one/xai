

#calss header
class _IMAGINATIVE():
	def __init__(self,): 
		self.name = "IMAGINATIVE"
		self.definitions = [u'new, original, and clever: ', u'good at thinking of new, original, and clever ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
