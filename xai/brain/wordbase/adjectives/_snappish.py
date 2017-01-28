

#calss header
class _SNAPPISH():
	def __init__(self,): 
		self.name = "SNAPPISH"
		self.definitions = [u'easily annoyed and often speaking in an angry way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
