

#calss header
class _HELPLESS():
	def __init__(self,): 
		self.name = "HELPLESS"
		self.definitions = [u'unable to do anything to help yourself or anyone else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
