

#calss header
class _INDULGENT():
	def __init__(self,): 
		self.name = "INDULGENT"
		self.definitions = [u'allowing someone to have or do what they want, especially when this is not good for them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
