

#calss header
class _ITALIC():
	def __init__(self,): 
		self.name = "ITALIC"
		self.definitions = [u'printed or written in italics: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
