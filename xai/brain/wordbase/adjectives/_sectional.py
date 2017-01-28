

#calss header
class _SECTIONAL():
	def __init__(self,): 
		self.name = "SECTIONAL"
		self.definitions = [u'A sectional piece of furniture is made up of parts that can be arranged in various ways: ', u'Interests or aims that are sectional are limited to a particular group within an organization, society, or country and do not consider other groups: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
