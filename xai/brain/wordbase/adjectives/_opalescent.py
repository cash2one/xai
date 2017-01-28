

#calss header
class _OPALESCENT():
	def __init__(self,): 
		self.name = "OPALESCENT"
		self.definitions = [u'Something that is opalescent reflects light and changes colour like an opal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
