

#calss header
class _UNITED():
	def __init__(self,): 
		self.name = "UNITED"
		self.definitions = [u'joined together as a group: ', u'If people are united, they all agree about something: ', u'an appearance of agreement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
