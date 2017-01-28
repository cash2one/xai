

#calss header
class _MACHO():
	def __init__(self,): 
		self.name = "MACHO"
		self.definitions = [u'behaving forcefully or showing no emotion in a way traditionally thought to be typical of a man: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
