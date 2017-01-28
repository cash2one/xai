

#calss header
class _INSENSIBLE():
	def __init__(self,): 
		self.name = "INSENSIBLE"
		self.definitions = [u'unconscious: ', u'to not care about something or be unwilling to react to it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
