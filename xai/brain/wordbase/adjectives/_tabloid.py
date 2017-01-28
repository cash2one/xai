

#calss header
class _TABLOID():
	def __init__(self,): 
		self.name = "TABLOID"
		self.definitions = [u'(of or relating to) a type of popular newspaper with small pages that has many pictures and short, simple reports: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
