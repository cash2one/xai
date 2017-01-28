

#calss header
class _TENURED():
	def __init__(self,): 
		self.name = "TENURED"
		self.definitions = [u'having been given tenure (= the right to remain permanently in a job, usually one in education): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
