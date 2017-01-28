

#calss header
class _VOLUBLE():
	def __init__(self,): 
		self.name = "VOLUBLE"
		self.definitions = [u'speaking a lot, with confidence and enthusiasm: ', u'involving a lot of words spoken confidently and forcefully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
