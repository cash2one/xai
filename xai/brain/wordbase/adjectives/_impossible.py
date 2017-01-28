

#calss header
class _IMPOSSIBLE():
	def __init__(self,): 
		self.name = "IMPOSSIBLE"
		self.definitions = [u'If an action or event is impossible, it cannot happen or be achieved: ', u'An impossible situation is extremely difficult to deal with or solve: ', u'An impossible person behaves very badly or is extremely difficult to deal with: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
