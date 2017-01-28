

#calss header
class _HIDEBOUND():
	def __init__(self,): 
		self.name = "HIDEBOUND"
		self.definitions = [u'having fixed opinions and ways of doing things and not willing to change or be influenced, especially by new or modern ideas']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
