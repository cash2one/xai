

#calss header
class _DISLOYAL():
	def __init__(self,): 
		self.name = "DISLOYAL"
		self.definitions = [u'not supporting someone that you should support: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
