

#calss header
class _ALLUSIVE():
	def __init__(self,): 
		self.name = "ALLUSIVE"
		self.definitions = [u'containing a lot of allusions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
