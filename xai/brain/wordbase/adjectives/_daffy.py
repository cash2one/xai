

#calss header
class _DAFFY():
	def __init__(self,): 
		self.name = "DAFFY"
		self.definitions = [u'strange or unusual, sometimes in a humorous way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
