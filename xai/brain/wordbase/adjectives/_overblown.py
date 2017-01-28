

#calss header
class _OVERBLOWN():
	def __init__(self,): 
		self.name = "OVERBLOWN"
		self.definitions = [u'bigger or more important or impressive than it should be: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
