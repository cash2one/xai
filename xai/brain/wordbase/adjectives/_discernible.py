

#calss header
class _DISCERNIBLE():
	def __init__(self,): 
		self.name = "DISCERNIBLE"
		self.definitions = [u'able to be seen or understood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
