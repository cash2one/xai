

#calss header
class _IMMOBILE():
	def __init__(self,): 
		self.name = "IMMOBILE"
		self.definitions = [u'not moving or not able to move: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
