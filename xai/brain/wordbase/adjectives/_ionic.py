

#calss header
class _IONIC():
	def __init__(self,): 
		self.name = "IONIC"
		self.definitions = [u'of or copying a style of ancient Greek building that has only a small amount of decoration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
