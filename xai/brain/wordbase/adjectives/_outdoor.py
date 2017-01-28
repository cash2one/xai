

#calss header
class _OUTDOOR():
	def __init__(self,): 
		self.name = "OUTDOOR"
		self.definitions = [u'existing, happening, or done outside, rather than inside a building: ', u'liking or relating to outdoor activities, such as walking and climbing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
