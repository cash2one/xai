

#calss header
class _LITHE():
	def __init__(self,): 
		self.name = "LITHE"
		self.definitions = [u'young, healthy, attractive, and able to move and bend smoothly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
