

#calss header
class _CALCULATING():
	def __init__(self,): 
		self.name = "CALCULATING"
		self.definitions = [u'often controlling situations for your own advantage in a way that is slightly unpleasant and causes people not to trust you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
