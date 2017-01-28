

#calss header
class _UNDERPRIVILEGED():
	def __init__(self,): 
		self.name = "UNDERPRIVILEGED"
		self.definitions = [u'without the money, possessions, education, opportunities, etc. that the average person has: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
