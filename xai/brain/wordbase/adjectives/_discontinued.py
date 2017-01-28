

#calss header
class _DISCONTINUED():
	def __init__(self,): 
		self.name = "DISCONTINUED"
		self.definitions = [u'A product or service that is discontinued is no longer being produced or offered: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
