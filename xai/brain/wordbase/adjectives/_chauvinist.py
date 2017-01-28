

#calss header
class _CHAUVINIST():
	def __init__(self,): 
		self.name = "CHAUVINIST"
		self.definitions = [u'believing or showing an unreasonable belief that your own country or race is the best or most important: ', u'believing that or behaving as if women are naturally less important, intelligent, or able than men: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
