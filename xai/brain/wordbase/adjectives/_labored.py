

#calss header
class _LABORED():
	def __init__(self,): 
		self.name = "LABORED"
		self.definitions = [u'US spelling of  laboured ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
