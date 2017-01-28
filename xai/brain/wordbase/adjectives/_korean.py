

#calss header
class _KOREAN():
	def __init__(self,): 
		self.name = "KOREAN"
		self.definitions = [u'belonging to or relating to North or South Korea, their people, or their language']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
