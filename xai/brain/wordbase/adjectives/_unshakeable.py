

#calss header
class _UNSHAKEABLE():
	def __init__(self,): 
		self.name = "UNSHAKEABLE"
		self.definitions = [u"If someone's trust or belief is unshakeable, it is firm and cannot be made weaker or destroyed: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
