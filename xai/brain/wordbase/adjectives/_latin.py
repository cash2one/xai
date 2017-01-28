

#calss header
class _LATIN():
	def __init__(self,): 
		self.name = "LATIN"
		self.definitions = [u'written in Latin: ', u'relating to (people or things in) countries that use a language that developed from Latin, such as French or Spanish: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
