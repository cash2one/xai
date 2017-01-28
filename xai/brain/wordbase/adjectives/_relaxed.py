

#calss header
class _RELAXED():
	def __init__(self,): 
		self.name = "RELAXED"
		self.definitions = [u'feeling happy and comfortable because nothing is worrying you: ', u'A relaxed situation or place is comfortable and informal: ', u'If someone is relaxed about something, they are not worried about it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
