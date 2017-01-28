

#calss header
class _STABBING():
	def __init__(self,): 
		self.name = "STABBING"
		self.definitions = [u'a sudden pain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
