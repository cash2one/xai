

#calss header
class _UNWORKABLE():
	def __init__(self,): 
		self.name = "UNWORKABLE"
		self.definitions = [u'An unworkable plan is not practical or cannot really be done successfully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
