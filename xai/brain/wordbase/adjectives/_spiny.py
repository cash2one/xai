

#calss header
class _SPINY():
	def __init__(self,): 
		self.name = "SPINY"
		self.definitions = [u'covered with spines (= long, sharp points like needles)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
