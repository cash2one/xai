

#calss header
class _HAPLESS():
	def __init__(self,): 
		self.name = "HAPLESS"
		self.definitions = [u'unlucky and usually unhappy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
