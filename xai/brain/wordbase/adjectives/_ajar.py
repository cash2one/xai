

#calss header
class _AJAR():
	def __init__(self,): 
		self.name = "AJAR"
		self.definitions = [u'If a door is ajar, it is slightly open: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
