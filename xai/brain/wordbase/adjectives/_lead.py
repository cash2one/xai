

#calss header
class _LEAD():
	def __init__(self,): 
		self.name = "LEAD"
		self.definitions = [u'used to describe the main performer or part in a performance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
