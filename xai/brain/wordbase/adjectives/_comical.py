

#calss header
class _COMICAL():
	def __init__(self,): 
		self.name = "COMICAL"
		self.definitions = [u'funny in a strange or silly way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
