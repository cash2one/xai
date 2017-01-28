

#calss header
class _STATIC():
	def __init__(self,): 
		self.name = "STATIC"
		self.definitions = [u'staying in one place without moving, or not changing for a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
