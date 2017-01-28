

#calss header
class _RAPACIOUS():
	def __init__(self,): 
		self.name = "RAPACIOUS"
		self.definitions = [u'having or showing a strong wish to take things for yourself, usually using unfair methods or force: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
