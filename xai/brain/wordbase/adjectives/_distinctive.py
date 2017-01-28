

#calss header
class _DISTINCTIVE():
	def __init__(self,): 
		self.name = "DISTINCTIVE"
		self.definitions = [u'Something that is distinctive is easy to recognize because it is different from other things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
