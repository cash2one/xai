

#calss header
class _THOUGHTFUL():
	def __init__(self,): 
		self.name = "THOUGHTFUL"
		self.definitions = [u'carefully considering things: ', u'quiet because you are thinking about something: ', u'kind and always thinking about how you can help other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
