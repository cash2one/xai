

#calss header
class _LEAKY():
	def __init__(self,): 
		self.name = "LEAKY"
		self.definitions = [u'Something that is leaky has a hole or crack in it that allows liquid or gas to get through: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
