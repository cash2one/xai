

#calss header
class _PERMANENT():
	def __init__(self,): 
		self.name = "PERMANENT"
		self.definitions = [u'lasting for a long time or for ever: ', u'Something that is permanent exists or happens all the time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
