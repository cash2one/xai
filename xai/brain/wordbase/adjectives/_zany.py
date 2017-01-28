

#calss header
class _ZANY():
	def __init__(self,): 
		self.name = "ZANY"
		self.definitions = [u'strange, surprising, or uncontrolled in a humorous way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
