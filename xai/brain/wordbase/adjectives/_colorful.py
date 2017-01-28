

#calss header
class _COLORFUL():
	def __init__(self,): 
		self.name = "COLORFUL"
		self.definitions = [u'US spelling of  colourful ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
