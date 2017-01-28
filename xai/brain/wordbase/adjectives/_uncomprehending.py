

#calss header
class _UNCOMPREHENDING():
	def __init__(self,): 
		self.name = "UNCOMPREHENDING"
		self.definitions = [u'not understanding something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
