

#calss header
class _EQUATORIAL():
	def __init__(self,): 
		self.name = "EQUATORIAL"
		self.definitions = [u'near the equator, or typical of places near the equator: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
