

#calss header
class _PICTORIAL():
	def __init__(self,): 
		self.name = "PICTORIAL"
		self.definitions = [u'shown in the form of a picture or photograph: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
