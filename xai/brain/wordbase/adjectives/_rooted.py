

#calss header
class _ROOTED():
	def __init__(self,): 
		self.name = "ROOTED"
		self.definitions = [u'having developed from something: ', u'very strong and firmly fixed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
