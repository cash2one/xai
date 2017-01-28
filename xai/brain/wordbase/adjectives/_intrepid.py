

#calss header
class _INTREPID():
	def __init__(self,): 
		self.name = "INTREPID"
		self.definitions = [u'extremely brave and showing no fear of dangerous situations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
