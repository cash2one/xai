

#calss header
class _DISPARAGING():
	def __init__(self,): 
		self.name = "DISPARAGING"
		self.definitions = [u'criticizing someone, in a way that shows you do not respect or value them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
