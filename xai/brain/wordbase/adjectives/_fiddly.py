

#calss header
class _FIDDLY():
	def __init__(self,): 
		self.name = "FIDDLY"
		self.definitions = [u'difficult to do because the parts involved are small: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
