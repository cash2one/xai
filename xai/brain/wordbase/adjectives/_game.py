

#calss header
class _GAME():
	def __init__(self,): 
		self.name = "GAME"
		self.definitions = [u'willing to do things that are new, difficult, or that involve risks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
