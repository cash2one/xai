

#calss header
class _PATRIARCHAL():
	def __init__(self,): 
		self.name = "PATRIARCHAL"
		self.definitions = [u'ruled or controlled by men: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
