

#calss header
class _GLASSY():
	def __init__(self,): 
		self.name = "GLASSY"
		self.definitions = [u'A glassy surface is smooth and shiny, like glass: ', u"If someone's eyes are glassy, they have a fixed expression and seem unable to see anything: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
