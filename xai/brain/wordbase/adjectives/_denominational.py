

#calss header
class _DENOMINATIONAL():
	def __init__(self,): 
		self.name = "DENOMINATIONAL"
		self.definitions = [u'connected with a particular religious denomination']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
