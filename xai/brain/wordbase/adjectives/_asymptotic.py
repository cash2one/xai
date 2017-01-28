

#calss header
class _ASYMPTOTIC():
	def __init__(self,): 
		self.name = "ASYMPTOTIC"
		self.definitions = [u'An asymptotic line is a line that gets closer and closer to a curve as the distance gets closer to infinity.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
