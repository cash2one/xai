

#calss header
class _ELFIN():
	def __init__(self,): 
		self.name = "ELFIN"
		self.definitions = [u'used to describe a person who is small and delicate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
