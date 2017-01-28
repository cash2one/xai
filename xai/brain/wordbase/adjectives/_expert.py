

#calss header
class _EXPERT():
	def __init__(self,): 
		self.name = "EXPERT"
		self.definitions = [u'having or showing a lot of knowledge or skill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
