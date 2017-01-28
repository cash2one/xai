

#calss header
class _AFFIRMATIVE():
	def __init__(self,): 
		self.name = "AFFIRMATIVE"
		self.definitions = [u'relating to a statement that shows agreement or says "yes": ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
