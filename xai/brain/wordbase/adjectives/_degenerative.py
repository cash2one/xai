

#calss header
class _DEGENERATIVE():
	def __init__(self,): 
		self.name = "DEGENERATIVE"
		self.definitions = [u'A degenerative illness is one in which the body or a part of the body gradually stops working: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
