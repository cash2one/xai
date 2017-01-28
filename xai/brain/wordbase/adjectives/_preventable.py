

#calss header
class _PREVENTABLE():
	def __init__(self,): 
		self.name = "PREVENTABLE"
		self.definitions = [u'able to be prevented: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
