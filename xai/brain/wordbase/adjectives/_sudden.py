

#calss header
class _SUDDEN():
	def __init__(self,): 
		self.name = "SUDDEN"
		self.definitions = [u'happening or done quickly and without warning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
