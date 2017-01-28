

#calss header
class _PREFABRICATED():
	def __init__(self,): 
		self.name = "PREFABRICATED"
		self.definitions = [u'Prefabricated buildings or objects are built from parts that have been made in a factory and can be put together quickly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
