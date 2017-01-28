

#calss header
class _RESISTANT():
	def __init__(self,): 
		self.name = "RESISTANT"
		self.definitions = [u'not wanting to accept something, especially changes or new ideas: ', u'not harmed or affected by something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
