

#calss header
class _SEAMED():
	def __init__(self,): 
		self.name = "SEAMED"
		self.definitions = [u'covered in lines: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
