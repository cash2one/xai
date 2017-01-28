

#calss header
class _FLOPPY():
	def __init__(self,): 
		self.name = "FLOPPY"
		self.definitions = [u'soft and not able to keep a firm shape or position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
