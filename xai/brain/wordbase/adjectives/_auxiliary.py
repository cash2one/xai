

#calss header
class _AUXILIARY():
	def __init__(self,): 
		self.name = "AUXILIARY"
		self.definitions = [u'giving help or support, especially to a more important person or thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
