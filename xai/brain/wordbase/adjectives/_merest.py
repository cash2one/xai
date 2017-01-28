

#calss header
class _MEREST():
	def __init__(self,): 
		self.name = "MEREST"
		self.definitions = [u'used to emphasize the surprising or strong effect of a very small action or event: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
