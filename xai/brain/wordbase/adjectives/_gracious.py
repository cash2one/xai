

#calss header
class _GRACIOUS():
	def __init__(self,): 
		self.name = "GRACIOUS"
		self.definitions = [u'behaving in a pleasant, polite, calm way: ', u'having the qualities of great comfort, beauty, and freedom made possible by being rich: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
