

#calss header
class _COCKAMAMIE():
	def __init__(self,): 
		self.name = "COCKAMAMIE"
		self.definitions = [u'stupid or silly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
