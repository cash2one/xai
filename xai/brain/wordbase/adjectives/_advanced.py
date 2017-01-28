

#calss header
class _ADVANCED():
	def __init__(self,): 
		self.name = "ADVANCED"
		self.definitions = [u'modern and well developed: ', u'at a higher, more difficult level: ', u'a school class that is doing work of a higher standard than is usual for students at that stage in their education']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
