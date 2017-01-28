

#calss header
class _EMPLOYABLE():
	def __init__(self,): 
		self.name = "EMPLOYABLE"
		self.definitions = [u'having enough skills and abilities for someone to employ you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
