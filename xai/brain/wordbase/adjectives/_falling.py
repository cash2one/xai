

#calss header
class _FALLING():
	def __init__(self,): 
		self.name = "FALLING"
		self.definitions = [u'If something is falling, it is becoming lower in size, amount, or strength: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
