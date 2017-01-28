

#calss header
class _METRO():
	def __init__(self,): 
		self.name = "METRO"
		self.definitions = [u'relating to a large city and the area surrounding it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
