

#calss header
class _HOODED():
	def __init__(self,): 
		self.name = "HOODED"
		self.definitions = [u'having a hood: ', u'Hooded eyelids are large and cover the eyes more than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
