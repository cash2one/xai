

#calss header
class _FABLED():
	def __init__(self,): 
		self.name = "FABLED"
		self.definitions = [u'used to refer to something or someone who has been made very famous, especially by having many stories written about it, him, or her: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
