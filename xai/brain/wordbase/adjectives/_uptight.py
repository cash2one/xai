

#calss header
class _UPTIGHT():
	def __init__(self,): 
		self.name = "UPTIGHT"
		self.definitions = [u'worried or nervous and not able to relax: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
