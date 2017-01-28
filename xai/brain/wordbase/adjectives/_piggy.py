

#calss header
class _PIGGY():
	def __init__(self,): 
		self.name = "PIGGY"
		self.definitions = [u'like a pig: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
