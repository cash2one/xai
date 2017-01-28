

#calss header
class _VIOLET():
	def __init__(self,): 
		self.name = "VIOLET"
		self.definitions = [u'having a bluish-purple colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
