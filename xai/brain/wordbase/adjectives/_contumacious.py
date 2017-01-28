

#calss header
class _CONTUMACIOUS():
	def __init__(self,): 
		self.name = "CONTUMACIOUS"
		self.definitions = [u'refusing to obey or respect the law in a way that shows contempt: ', u'refusing to obey or show respect']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
