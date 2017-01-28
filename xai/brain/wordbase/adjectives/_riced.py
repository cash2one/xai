

#calss header
class _RICED():
	def __init__(self,): 
		self.name = "RICED"
		self.definitions = [u'separated into very small pieces that look like rice by being forced through small holes in a special tool: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
