

#calss header
class _HARASSED():
	def __init__(self,): 
		self.name = "HARASSED"
		self.definitions = [u'worried, annoyed, and tired, especially because you have too many things to deal with: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
