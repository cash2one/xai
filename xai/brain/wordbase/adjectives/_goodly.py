

#calss header
class _GOODLY():
	def __init__(self,): 
		self.name = "GOODLY"
		self.definitions = [u'great or large: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
