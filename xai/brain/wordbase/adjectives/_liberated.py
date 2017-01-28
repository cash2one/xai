

#calss header
class _LIBERATED():
	def __init__(self,): 
		self.name = "LIBERATED"
		self.definitions = [u'not following traditional ways of behaving or old ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
