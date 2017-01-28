

#calss header
class _UNCONSTITUTIONAL():
	def __init__(self,): 
		self.name = "UNCONSTITUTIONAL"
		self.definitions = [u'not allowed by the constitution (= set of rules for government) of a country or organization: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
