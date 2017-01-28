

#calss header
class _STYLISH():
	def __init__(self,): 
		self.name = "STYLISH"
		self.definitions = [u'of a high quality in appearance, design, or behaviour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
