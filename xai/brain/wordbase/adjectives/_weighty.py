

#calss header
class _WEIGHTY():
	def __init__(self,): 
		self.name = "WEIGHTY"
		self.definitions = [u'heavy: ', u'A weighty subject, book, or piece of work is important or serious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
