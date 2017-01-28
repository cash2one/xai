

#calss header
class _RUNNING():
	def __init__(self,): 
		self.name = "RUNNING"
		self.definitions = [u'happening on a particular number of regular occasions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
