

#calss header
class _RESTIVE():
	def __init__(self,): 
		self.name = "RESTIVE"
		self.definitions = [u'unwilling to be controlled or be patient: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
