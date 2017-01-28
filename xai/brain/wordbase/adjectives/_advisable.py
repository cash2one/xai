

#calss header
class _ADVISABLE():
	def __init__(self,): 
		self.name = "ADVISABLE"
		self.definitions = [u'If something is advisable, it will avoid problems if you do it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
