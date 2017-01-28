

#calss header
class _LEGGY():
	def __init__(self,): 
		self.name = "LEGGY"
		self.definitions = [u'A leggy woman or girl has long legs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
