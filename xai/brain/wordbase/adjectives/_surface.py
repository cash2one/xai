

#calss header
class _SURFACE():
	def __init__(self,): 
		self.name = "SURFACE"
		self.definitions = [u'working or operating on the top of the land or sea, rather than under the land or sea, or by air', u'appearing in a particular way but not always showing the truth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
