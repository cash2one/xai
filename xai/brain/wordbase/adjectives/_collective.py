

#calss header
class _COLLECTIVE():
	def __init__(self,): 
		self.name = "COLLECTIVE"
		self.definitions = [u'of or shared by every member of a group of people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
