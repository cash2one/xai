

#calss header
class _SCREWY():
	def __init__(self,): 
		self.name = "SCREWY"
		self.definitions = [u'very strange, silly, or unusual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
