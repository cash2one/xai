

#calss header
class _ALTERNATE():
	def __init__(self,): 
		self.name = "ALTERNATE"
		self.definitions = [u'with first one thing, then another thing, and then the first thing again: ', u'If something happens on alternate days, it happens every second day: ', u'An alternate plan or method is one that you can use if you do not want to use another one.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
