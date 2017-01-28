

#calss header
class _BEACHED():
	def __init__(self,): 
		self.name = "BEACHED"
		self.definitions = [u'A beached whale, dolphin, etc. has swum onto a beach and cannot get back into the water.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
