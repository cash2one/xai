

#calss header
class _LADYLIKE():
	def __init__(self,): 
		self.name = "LADYLIKE"
		self.definitions = [u'graceful, polite, and behaving in a way that is thought to be socially acceptable for a woman: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
