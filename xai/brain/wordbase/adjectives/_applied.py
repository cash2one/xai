

#calss header
class _APPLIED():
	def __init__(self,): 
		self.name = "APPLIED"
		self.definitions = [u'relating to a subject of study, especially a science, that has a practical use: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
