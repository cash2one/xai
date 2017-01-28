

#calss header
class _BOTHERED():
	def __init__(self,): 
		self.name = "BOTHERED"
		self.definitions = [u'If you are bothered about something, it is important to you and you are worried about it: ', u'If you are not bothered about something, it is not important to you or does not worry you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
