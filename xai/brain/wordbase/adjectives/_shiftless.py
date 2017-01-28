

#calss header
class _SHIFTLESS():
	def __init__(self,): 
		self.name = "SHIFTLESS"
		self.definitions = [u'lazy and not having much determination or a clear purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
