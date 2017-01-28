

#calss header
class _ARCH():
	def __init__(self,): 
		self.name = "ARCH"
		self.definitions = [u'showing that you think it is amusing that you know more about something than someone else does: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
