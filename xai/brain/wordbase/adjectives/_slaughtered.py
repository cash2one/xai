

#calss header
class _SLAUGHTERED():
	def __init__(self,): 
		self.name = "SLAUGHTERED"
		self.definitions = [u'to get very drunk']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
