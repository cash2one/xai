

#calss header
class _BACTERIAL():
	def __init__(self,): 
		self.name = "BACTERIAL"
		self.definitions = [u'caused by, made from, or relating to bacteria: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
