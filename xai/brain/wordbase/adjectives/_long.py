

#calss header
class _LONG():
	def __init__(self,): 
		self.name = "LONG"
		self.definitions = [u'continuing for a large amount of time: ', u'being a distance between two points that is more than average or usual: ', u'used to describe a piece of writing that has a lot of pages or words: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
