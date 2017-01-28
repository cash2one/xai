

#calss header
class _INANE():
	def __init__(self,): 
		self.name = "INANE"
		self.definitions = [u'extremely silly or with no real meaning or importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
