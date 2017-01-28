

#calss header
class _STRANGULATED():
	def __init__(self,): 
		self.name = "STRANGULATED"
		self.definitions = [u'If an organ or other part inside the body is strangulated, it has become tightly pressed, blocking the flow of blood or air through it: ', u'A strangulated sound is not full or relaxed, but made when your throat is tight, for example because of fear or anger: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
