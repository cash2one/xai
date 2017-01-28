

#calss header
class _UNWIELDY():
	def __init__(self,): 
		self.name = "UNWIELDY"
		self.definitions = [u'An unwieldy object is difficult to move or handle because it is heavy, large, or a strange shape: ', u'An unwieldy system is slow and not effective, usually because it is too big, badly organized, or involves too many different organizations or people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
