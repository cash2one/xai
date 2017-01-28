

#calss header
class _WALLED():
	def __init__(self,): 
		self.name = "WALLED"
		self.definitions = [u'surrounded by a wall: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
