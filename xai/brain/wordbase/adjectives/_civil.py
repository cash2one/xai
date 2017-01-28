

#calss header
class _CIVIL():
	def __init__(self,): 
		self.name = "CIVIL"
		self.definitions = [u'not military or religious, or relating to the ordinary people of a country: ', u'relating to private arguments between people or organizations rather than criminal matters: ', u'polite and formal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
