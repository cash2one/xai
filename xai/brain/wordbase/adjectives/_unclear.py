

#calss header
class _UNCLEAR():
	def __init__(self,): 
		self.name = "UNCLEAR"
		self.definitions = [u'not obvious or easy to see or know: ', u'If you are unclear about something, you are not certain about it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
