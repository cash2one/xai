

#calss header
class _CORKED():
	def __init__(self,): 
		self.name = "CORKED"
		self.definitions = [u'Wine is described as corked if its taste has been spoiled by the cork.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
