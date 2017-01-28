

#calss header
class _DANDY():
	def __init__(self,): 
		self.name = "DANDY"
		self.definitions = [u'very good. This is often said as a joke when really something is not good or you are not happy about it : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
