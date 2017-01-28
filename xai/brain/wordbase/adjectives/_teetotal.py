

#calss header
class _TEETOTAL():
	def __init__(self,): 
		self.name = "TEETOTAL"
		self.definitions = [u'never drinking alcohol or opposed to the drinking of alcohol']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
