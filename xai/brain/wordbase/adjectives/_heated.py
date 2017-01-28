

#calss header
class _HEATED():
	def __init__(self,): 
		self.name = "HEATED"
		self.definitions = [u'made hot or warm: ', u'excited or angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
