

#calss header
class _MATERIALISTIC():
	def __init__(self,): 
		self.name = "MATERIALISTIC"
		self.definitions = [u'believing that having money and possessions is the most important thing in life']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
