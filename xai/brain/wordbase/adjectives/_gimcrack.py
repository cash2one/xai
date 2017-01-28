

#calss header
class _GIMCRACK():
	def __init__(self,): 
		self.name = "GIMCRACK"
		self.definitions = [u'attractive on the surface but badly made and of no real or permanent value']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
