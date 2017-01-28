

#calss header
class _STUPID():
	def __init__(self,): 
		self.name = "STUPID"
		self.definitions = [u'silly or unwise; showing poor judgment or little intelligence: ', u'annoying, or causing a problem: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
