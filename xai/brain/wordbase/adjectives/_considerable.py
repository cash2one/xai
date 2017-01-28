

#calss header
class _CONSIDERABLE():
	def __init__(self,): 
		self.name = "CONSIDERABLE"
		self.definitions = [u'large or of noticeable importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
