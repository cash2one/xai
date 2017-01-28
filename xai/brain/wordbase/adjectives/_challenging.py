

#calss header
class _CHALLENGING():
	def __init__(self,): 
		self.name = "CHALLENGING"
		self.definitions = [u'difficult, in a way that tests your ability or determination: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
