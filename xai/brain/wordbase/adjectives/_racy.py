

#calss header
class _RACY():
	def __init__(self,): 
		self.name = "RACY"
		self.definitions = [u'exciting and slightly shocking, especially because of relating to or suggesting sex: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
