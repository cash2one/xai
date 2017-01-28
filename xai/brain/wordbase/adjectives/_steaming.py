

#calss header
class _STEAMING():
	def __init__(self,): 
		self.name = "STEAMING"
		self.definitions = [u'producing steam: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
