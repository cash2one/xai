

#calss header
class _RECENT():
	def __init__(self,): 
		self.name = "RECENT"
		self.definitions = [u'happening or starting from a short time ago: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
