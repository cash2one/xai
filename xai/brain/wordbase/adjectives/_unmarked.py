

#calss header
class _UNMARKED():
	def __init__(self,): 
		self.name = "UNMARKED"
		self.definitions = [u'having no signs or marks showing what something is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
