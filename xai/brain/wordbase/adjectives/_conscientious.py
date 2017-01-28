

#calss header
class _CONSCIENTIOUS():
	def __init__(self,): 
		self.name = "CONSCIENTIOUS"
		self.definitions = [u'putting a lot of effort into your work: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
