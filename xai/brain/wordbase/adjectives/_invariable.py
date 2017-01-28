

#calss header
class _INVARIABLE():
	def __init__(self,): 
		self.name = "INVARIABLE"
		self.definitions = [u'staying the same and never changing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
