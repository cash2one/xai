

#calss header
class _BREADED():
	def __init__(self,): 
		self.name = "BREADED"
		self.definitions = [u'covered in breadcrumbs before being cooked: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
