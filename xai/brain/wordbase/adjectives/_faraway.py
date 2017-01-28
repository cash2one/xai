

#calss header
class _FARAWAY():
	def __init__(self,): 
		self.name = "FARAWAY"
		self.definitions = [u'a long way away: ', u'If you have a faraway expression, you look as though you are not thinking about what is happening around you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
