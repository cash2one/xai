

#calss header
class _SUPERSONIC():
	def __init__(self,): 
		self.name = "SUPERSONIC"
		self.definitions = [u'faster than the speed of sound: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
