

#calss header
class _UNDERARM():
	def __init__(self,): 
		self.name = "UNDERARM"
		self.definitions = [u'of or for use in the armpit (= hollow place under the arm where the arm joins the body): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
