

#calss header
class _BEST():
	def __init__(self,): 
		self.name = "BEST"
		self.definitions = [u'of the highest quality, or being the most suitable, pleasing, or effective type of thing or person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
