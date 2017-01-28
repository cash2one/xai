

#calss header
class _INADVISABLE():
	def __init__(self,): 
		self.name = "INADVISABLE"
		self.definitions = [u'unwise and likely to have unwanted results, and therefore worth avoiding: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
