

#calss header
class _RECTAL():
	def __init__(self,): 
		self.name = "RECTAL"
		self.definitions = [u'relating to the rectum (= the last section of the large bowel): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
