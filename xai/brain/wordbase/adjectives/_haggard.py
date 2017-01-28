

#calss header
class _HAGGARD():
	def __init__(self,): 
		self.name = "HAGGARD"
		self.definitions = [u'looking ill or tired, often with dark skin under the eyes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
