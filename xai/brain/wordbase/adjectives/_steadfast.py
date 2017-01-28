

#calss header
class _STEADFAST():
	def __init__(self,): 
		self.name = "STEADFAST"
		self.definitions = [u'staying the same for a long time and not changing quickly or unexpectedly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
