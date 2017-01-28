

#calss header
class _FRIVOLOUS():
	def __init__(self,): 
		self.name = "FRIVOLOUS"
		self.definitions = [u'behaving in a silly way and not taking anything seriously: ', u'A frivolous activity or object is silly or not important rather than useful or serious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
