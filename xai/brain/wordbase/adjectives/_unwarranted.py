

#calss header
class _UNWARRANTED():
	def __init__(self,): 
		self.name = "UNWARRANTED"
		self.definitions = [u'not having a good reason and therefore annoying or unfair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
