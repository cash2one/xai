

#calss header
class _UNLIMITED():
	def __init__(self,): 
		self.name = "UNLIMITED"
		self.definitions = [u'not limited; having the greatest possible amount, number, or level: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
