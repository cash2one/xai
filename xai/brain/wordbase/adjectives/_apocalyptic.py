

#calss header
class _APOCALYPTIC():
	def __init__(self,): 
		self.name = "APOCALYPTIC"
		self.definitions = [u'showing or describing the total destruction and end of the world, or extremely bad future events: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
