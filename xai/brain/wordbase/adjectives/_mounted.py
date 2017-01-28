

#calss header
class _MOUNTED():
	def __init__(self,): 
		self.name = "MOUNTED"
		self.definitions = [u'Mounted soldiers or police officers ride horses while on duty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
