

#calss header
class _MAKESHIFT():
	def __init__(self,): 
		self.name = "MAKESHIFT"
		self.definitions = [u'temporary and of low quality, but used because of a sudden need: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
