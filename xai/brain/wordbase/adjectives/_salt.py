

#calss header
class _SALT():
	def __init__(self,): 
		self.name = "SALT"
		self.definitions = [u'containing or preserved in salt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
