

#calss header
class _HERMETIC():
	def __init__(self,): 
		self.name = "HERMETIC"
		self.definitions = [u'(of a container) so tightly closed that no air can leave or enter: ', u"If a particular group is hermetic, the people who live within it don't often communicate with those who live outside it: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
