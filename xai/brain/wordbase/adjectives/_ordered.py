

#calss header
class _ORDERED():
	def __init__(self,): 
		self.name = "ORDERED"
		self.definitions = [u'carefully arranged or controlled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
