

#calss header
class _SYNONYMOUS():
	def __init__(self,): 
		self.name = "SYNONYMOUS"
		self.definitions = [u'having the same meaning: ', u"If you say that one thing is synonymous with another, you mean that the two things are so closely connected in most people's minds that one suggests the other: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
