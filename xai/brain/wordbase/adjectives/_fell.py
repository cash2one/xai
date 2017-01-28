

#calss header
class _FELL():
	def __init__(self,): 
		self.name = "FELL"
		self.definitions = [u'evil or cruel', u'relating to fells (= hills): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
