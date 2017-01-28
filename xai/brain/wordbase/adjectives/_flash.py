

#calss header
class _FLASH():
	def __init__(self,): 
		self.name = "FLASH"
		self.definitions = [u'looking expensive in a way that attracts attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
