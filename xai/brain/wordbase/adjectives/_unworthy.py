

#calss header
class _UNWORTHY():
	def __init__(self,): 
		self.name = "UNWORTHY"
		self.definitions = [u'not deserving respect, admiration, or support: ', u'not deserving to be considered, given attention, etc.: ', u'not suitable for or characteristic of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
