

#calss header
class _RESIGNED():
	def __init__(self,): 
		self.name = "RESIGNED"
		self.definitions = [u'accepting that something you do not like will happen because you cannot change it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
