

#calss header
class _NATTY():
	def __init__(self,): 
		self.name = "NATTY"
		self.definitions = [u'stylish and tidy in every detail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
