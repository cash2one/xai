

#calss header
class _SEPARATE():
	def __init__(self,): 
		self.name = "SEPARATE"
		self.definitions = [u'existing or happening independently or in a different physical space: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
