

#calss header
class _UNPRONOUNCEABLE():
	def __init__(self,): 
		self.name = "UNPRONOUNCEABLE"
		self.definitions = [u'difficult to say or (of something written) difficult to know how to say: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
