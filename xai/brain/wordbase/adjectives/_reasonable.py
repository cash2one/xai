

#calss header
class _REASONABLE():
	def __init__(self,): 
		self.name = "REASONABLE"
		self.definitions = [u'based on or using good judgment and therefore fair and practical: ', u'acceptable: ', u'not too expensive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
