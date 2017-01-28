

#calss header
class _DISAFFECTED():
	def __init__(self,): 
		self.name = "DISAFFECTED"
		self.definitions = [u'no longer supporting or being satisfied with an organization or idea: ', u"Young people who are disaffected are no longer satisfied with society's values: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
