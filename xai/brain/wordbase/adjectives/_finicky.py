

#calss header
class _FINICKY():
	def __init__(self,): 
		self.name = "FINICKY"
		self.definitions = [u'difficult to please: ', u'needing a lot of attention to detail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
