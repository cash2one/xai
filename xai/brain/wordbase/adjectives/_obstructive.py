

#calss header
class _OBSTRUCTIVE():
	def __init__(self,): 
		self.name = "OBSTRUCTIVE"
		self.definitions = [u'trying to stop someone from doing something by causing problems for them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
