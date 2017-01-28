

#calss header
class _FRACTIOUS():
	def __init__(self,): 
		self.name = "FRACTIOUS"
		self.definitions = [u'easily upset or annoyed, and often complaining: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
