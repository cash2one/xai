

#calss header
class _DECADENT():
	def __init__(self,): 
		self.name = "DECADENT"
		self.definitions = [u'A decadent person or group has low moral standards: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
