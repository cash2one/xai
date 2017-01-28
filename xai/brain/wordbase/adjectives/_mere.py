

#calss header
class _MERE():
	def __init__(self,): 
		self.name = "MERE"
		self.definitions = [u'used to emphasize that something is not large or important: ', u'used to emphasize how strongly someone feels about something or how extreme a situation is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
