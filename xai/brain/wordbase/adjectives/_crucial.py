

#calss header
class _CRUCIAL():
	def __init__(self,): 
		self.name = "CRUCIAL"
		self.definitions = [u'extremely important or necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
