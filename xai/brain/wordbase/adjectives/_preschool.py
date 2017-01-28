

#calss header
class _PRESCHOOL():
	def __init__(self,): 
		self.name = "PRESCHOOL"
		self.definitions = [u'of or relating to children who are between about three and five years old and have not yet gone to school, and their activities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
