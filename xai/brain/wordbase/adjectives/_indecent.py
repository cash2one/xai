

#calss header
class _INDECENT():
	def __init__(self,): 
		self.name = "INDECENT"
		self.definitions = [u'morally offensive, especially in a sexual way: ', u'not suitable or correct for a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
