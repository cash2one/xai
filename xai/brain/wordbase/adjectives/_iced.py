

#calss header
class _ICED():
	def __init__(self,): 
		self.name = "ICED"
		self.definitions = [u'An iced drink has been made very cold, usually by having ice added to it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
