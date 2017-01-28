

#calss header
class _WRECKED():
	def __init__(self,): 
		self.name = "WRECKED"
		self.definitions = [u'very badly damaged: ', u'very drunk: ', u'very tired']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
