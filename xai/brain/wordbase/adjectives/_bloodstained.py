

#calss header
class _BLOODSTAINED():
	def __init__(self,): 
		self.name = "BLOODSTAINED"
		self.definitions = [u'with marks of blood on it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
