

#calss header
class _CRACKERJACK():
	def __init__(self,): 
		self.name = "CRACKERJACK"
		self.definitions = [u'excellent, of the highest standard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
