

#calss header
class _OCULAR():
	def __init__(self,): 
		self.name = "OCULAR"
		self.definitions = [u'of or related to the eyes or sight']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
