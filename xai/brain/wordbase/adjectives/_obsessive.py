

#calss header
class _OBSESSIVE():
	def __init__(self,): 
		self.name = "OBSESSIVE"
		self.definitions = [u'thinking about something or someone, or doing something, too much or all the time: ', u'like, typical of, or caused by an obsession: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
