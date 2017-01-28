

#calss header
class _PARENTAL():
	def __init__(self,): 
		self.name = "PARENTAL"
		self.definitions = [u'relating to parents or to being a parent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
