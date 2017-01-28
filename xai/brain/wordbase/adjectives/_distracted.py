

#calss header
class _DISTRACTED():
	def __init__(self,): 
		self.name = "DISTRACTED"
		self.definitions = [u'nervous or confused because you are worried about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
