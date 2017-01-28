

#calss header
class _EXPOSED():
	def __init__(self,): 
		self.name = "EXPOSED"
		self.definitions = [u'having no protection from bad weather: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
