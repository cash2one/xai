

#calss header
class _PRECARIOUS():
	def __init__(self,): 
		self.name = "PRECARIOUS"
		self.definitions = [u'in a dangerous state because of not being safe or not being held in place firmly: ', u'A precarious situation is likely to get worse: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
