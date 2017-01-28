

#calss header
class _BUSINESSLIKE():
	def __init__(self,): 
		self.name = "BUSINESSLIKE"
		self.definitions = [u'getting things done in a quick and practical way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
