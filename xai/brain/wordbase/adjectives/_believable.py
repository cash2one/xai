

#calss header
class _BELIEVABLE():
	def __init__(self,): 
		self.name = "BELIEVABLE"
		self.definitions = [u'If something is believable, it seems possible, real, or true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
