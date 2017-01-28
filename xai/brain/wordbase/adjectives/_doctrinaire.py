

#calss header
class _DOCTRINAIRE():
	def __init__(self,): 
		self.name = "DOCTRINAIRE"
		self.definitions = [u'based on and following fixed beliefs rather than considering practical problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
