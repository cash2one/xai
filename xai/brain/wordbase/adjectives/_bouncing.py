

#calss header
class _BOUNCING():
	def __init__(self,): 
		self.name = "BOUNCING"
		self.definitions = [u'(especially of a baby) healthy and energetic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
