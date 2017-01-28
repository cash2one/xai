

#calss header
class _PUBESCENT():
	def __init__(self,): 
		self.name = "PUBESCENT"
		self.definitions = [u'A pubescent child is at the stage in life when they are developing from a child into an adult and becoming able to have children: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
