

#calss header
class _COMPLICATED():
	def __init__(self,): 
		self.name = "COMPLICATED"
		self.definitions = [u'involving a lot of different parts, in a way that is difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
