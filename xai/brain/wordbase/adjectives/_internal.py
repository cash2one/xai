

#calss header
class _INTERNAL():
	def __init__(self,): 
		self.name = "INTERNAL"
		self.definitions = [u'existing or happening inside a person, object, organization, place, or country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
