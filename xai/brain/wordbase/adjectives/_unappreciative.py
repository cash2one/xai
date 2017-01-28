

#calss header
class _UNAPPRECIATIVE():
	def __init__(self,): 
		self.name = "UNAPPRECIATIVE"
		self.definitions = [u'not showing that you understand how good something is, or not grateful for something']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
