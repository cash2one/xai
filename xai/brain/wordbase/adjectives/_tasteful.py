

#calss header
class _TASTEFUL():
	def __init__(self,): 
		self.name = "TASTEFUL"
		self.definitions = [u'attractive and chosen for style and quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
