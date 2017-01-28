

#calss header
class _DUD():
	def __init__(self,): 
		self.name = "DUD"
		self.definitions = [u'not working or not having any value: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
