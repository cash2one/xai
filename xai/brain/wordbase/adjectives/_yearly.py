

#calss header
class _YEARLY():
	def __init__(self,): 
		self.name = "YEARLY"
		self.definitions = [u'every year or once every year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
