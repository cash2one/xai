

#calss header
class _BOTHERSOME():
	def __init__(self,): 
		self.name = "BOTHERSOME"
		self.definitions = [u'annoying or causing trouble: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
