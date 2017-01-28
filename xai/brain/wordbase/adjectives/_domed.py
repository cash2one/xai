

#calss header
class _DOMED():
	def __init__(self,): 
		self.name = "DOMED"
		self.definitions = [u'shaped like a dome or covered with a dome']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
