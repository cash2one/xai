

#calss header
class _MANDATORY():
	def __init__(self,): 
		self.name = "MANDATORY"
		self.definitions = [u'Something that is mandatory must be done, or is demanded by law: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
