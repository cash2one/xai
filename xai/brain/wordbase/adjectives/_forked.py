

#calss header
class _FORKED():
	def __init__(self,): 
		self.name = "FORKED"
		self.definitions = [u'with one end divided into two parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
