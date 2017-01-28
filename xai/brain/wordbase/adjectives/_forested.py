

#calss header
class _FORESTED():
	def __init__(self,): 
		self.name = "FORESTED"
		self.definitions = [u'covered in forest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
