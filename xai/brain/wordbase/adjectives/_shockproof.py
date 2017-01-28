

#calss header
class _SHOCKPROOF():
	def __init__(self,): 
		self.name = "SHOCKPROOF"
		self.definitions = [u'A shockproof watch or other device is not easily damaged if hit or dropped.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
