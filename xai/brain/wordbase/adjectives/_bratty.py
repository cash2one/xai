

#calss header
class _BRATTY():
	def __init__(self,): 
		self.name = "BRATTY"
		self.definitions = [u'a bratty child or person behaves badly, especially because they expect to get everything that they want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
