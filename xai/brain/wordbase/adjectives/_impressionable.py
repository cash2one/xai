

#calss header
class _IMPRESSIONABLE():
	def __init__(self,): 
		self.name = "IMPRESSIONABLE"
		self.definitions = [u'easily influenced by other people, especially because you are young: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
