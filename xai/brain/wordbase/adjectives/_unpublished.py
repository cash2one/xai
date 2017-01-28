

#calss header
class _UNPUBLISHED():
	def __init__(self,): 
		self.name = "UNPUBLISHED"
		self.definitions = [u'written but not yet published: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
