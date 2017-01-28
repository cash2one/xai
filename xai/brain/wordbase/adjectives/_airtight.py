

#calss header
class _AIRTIGHT():
	def __init__(self,): 
		self.name = "AIRTIGHT"
		self.definitions = [u'completely closed so that no air can get in or out: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
