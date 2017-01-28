

#calss header
class _HORIZONTAL():
	def __init__(self,): 
		self.name = "HORIZONTAL"
		self.definitions = [u'parallel to the ground or to the bottom or top edge of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
