

#calss header
class _HOMELESS():
	def __init__(self,): 
		self.name = "HOMELESS"
		self.definitions = [u'without a home: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
