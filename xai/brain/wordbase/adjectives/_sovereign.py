

#calss header
class _SOVEREIGN():
	def __init__(self,): 
		self.name = "SOVEREIGN"
		self.definitions = [u'having the highest power or being completely independent: ', u'an extremely successful way of dealing with a problem: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
