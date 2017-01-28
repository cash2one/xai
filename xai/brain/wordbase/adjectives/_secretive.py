

#calss header
class _SECRETIVE():
	def __init__(self,): 
		self.name = "SECRETIVE"
		self.definitions = [u'People who are secretive hide their feelings, thoughts, intentions, and actions from other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
