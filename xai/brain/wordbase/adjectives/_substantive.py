

#calss header
class _SUBSTANTIVE():
	def __init__(self,): 
		self.name = "SUBSTANTIVE"
		self.definitions = [u'important, serious, or related to real facts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
