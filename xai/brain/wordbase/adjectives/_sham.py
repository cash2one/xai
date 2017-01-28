

#calss header
class _SHAM():
	def __init__(self,): 
		self.name = "SHAM"
		self.definitions = [u'only pretending to be real; false: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
