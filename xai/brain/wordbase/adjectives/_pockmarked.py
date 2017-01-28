

#calss header
class _POCKMARKED():
	def __init__(self,): 
		self.name = "POCKMARKED"
		self.definitions = [u'marked with pockmarks: ', u'A pockmarked surface has a lot of holes or low areas in it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
