

#calss header
class _FORENSIC():
	def __init__(self,): 
		self.name = "FORENSIC"
		self.definitions = [u'related to scientific methods of solving crimes, involving examining the objects or substances that are involved in the crime: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
