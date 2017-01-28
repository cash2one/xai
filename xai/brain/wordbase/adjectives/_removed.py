

#calss header
class _REMOVED():
	def __init__(self,): 
		self.name = "REMOVED"
		self.definitions = [u'used to refer to a cousin (= a relation) separated from you by one, two, etc. generations (= same family age groups): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
