

#calss header
class _CALLOUSED():
	def __init__(self,): 
		self.name = "CALLOUSED"
		self.definitions = [u'If feet or hands are calloused, they are covered with hard areas of skin.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
