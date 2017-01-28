

#calss header
class _VAINGLORIOUS():
	def __init__(self,): 
		self.name = "VAINGLORIOUS"
		self.definitions = [u'showing too much pride in your own abilities or achievements: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
