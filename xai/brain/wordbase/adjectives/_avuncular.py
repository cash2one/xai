

#calss header
class _AVUNCULAR():
	def __init__(self,): 
		self.name = "AVUNCULAR"
		self.definitions = [u'friendly, kind, or helpful, like the expected behaviour of an uncle: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
