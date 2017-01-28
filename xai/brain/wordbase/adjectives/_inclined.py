

#calss header
class _INCLINED():
	def __init__(self,): 
		self.name = "INCLINED"
		self.definitions = [u'likely or wanting to do something: ', u'having natural artistic, technical, etc. ability: ', u'to have an opinion about something, but not a strong opinion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
