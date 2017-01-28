

#calss header
class _OFFICIALLY():
	def __init__(self,): 
		self.name = "OFFICIALLY"
		self.definitions = [u'formally and in a way agreed to or arranged by people in positions of authority: ', u'as stated or accepted by people publicly but not privately or as things really are: ', u'in or relating to a position of responsibility that you hold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
