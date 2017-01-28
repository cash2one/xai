

#calss header
class _CONSTITUTIONALLY():
	def __init__(self,): 
		self.name = "CONSTITUTIONALLY"
		self.definitions = [u'according to the rules in a constitution: ', u'in a way that relates to or is caused by your general health or your character: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
