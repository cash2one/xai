

#calss header
class _FRIABLE():
	def __init__(self,): 
		self.name = "FRIABLE"
		self.definitions = [u'easily broken into small pieces']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
