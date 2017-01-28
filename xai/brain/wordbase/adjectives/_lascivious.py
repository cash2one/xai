

#calss header
class _LASCIVIOUS():
	def __init__(self,): 
		self.name = "LASCIVIOUS"
		self.definitions = [u'expressing a strong desire for sexual activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
