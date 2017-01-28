

#calss header
class _INTERNECINE():
	def __init__(self,): 
		self.name = "INTERNECINE"
		self.definitions = [u'Internecine war or fighting happens between members of the same group, religion, or country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
