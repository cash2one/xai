

#calss header
class _REFRESHED():
	def __init__(self,): 
		self.name = "REFRESHED"
		self.definitions = [u'less hot or tired: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
