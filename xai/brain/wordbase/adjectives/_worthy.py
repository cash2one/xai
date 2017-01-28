

#calss header
class _WORTHY():
	def __init__(self,): 
		self.name = "WORTHY"
		self.definitions = [u'deserving respect, admiration, or support: ', u'deserving to be given attention, noticed, etc.: ', u'Something that is worthy is not very interesting but should be admired for its good and useful qualities: ', u'suitable for or characteristic of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
