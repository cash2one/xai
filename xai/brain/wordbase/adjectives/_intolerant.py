

#calss header
class _INTOLERANT():
	def __init__(self,): 
		self.name = "INTOLERANT"
		self.definitions = [u'disapproving of or refusing to accept ideas or ways of behaving that are different from your own: ', u'used, usually in compounds, to describe a person who is not able to eat a particular type of food or take a particular type of medicine without it having a bad effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
