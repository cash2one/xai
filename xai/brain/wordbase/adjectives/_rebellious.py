

#calss header
class _REBELLIOUS():
	def __init__(self,): 
		self.name = "REBELLIOUS"
		self.definitions = [u'If a group of people are rebellious, they oppose the ideas of the people in authority and plan to change the system, often using force: ', u'If someone is rebellious, they are difficult to control and do not behave in the way that is expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
