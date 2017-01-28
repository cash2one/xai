

#calss header
class _KEPT():
	def __init__(self,): 
		self.name = "KEPT"
		self.definitions = [u'someone who does not work but is instead given money and a place to live by the person she or he is having a sexual relationship with']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
