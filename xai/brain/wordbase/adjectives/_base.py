

#calss header
class _BASE():
	def __init__(self,): 
		self.name = "BASE"
		self.definitions = [u'not showing any honour and having no morals: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
